from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from googleplaces import GooglePlaces, types, lang
import os
from .models import Winery, Tour, User
from django.db.models import Q

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

@login_required
def profile(request):
    tours = Tour.objects.filter(user=request.user.id)     
    return render (request, 'profile.html', {'tours': tours})

def recommendedtrips(request):
    return render(request, 'recommended-trips.html')

def stop_reorder(request, tour_id):
  data = request.POST.copy()
  tour = Tour.objects.get(id=tour_id)
  position = int(data['position'])
  stops = list(filter(None, tour.stops.split(',')))
  stops_copy = stops.copy()
  try:
    if data['moveup'] and position >= 1:
      stops[position - 1] = stops[position]
      stops[position] = stops_copy[position - 1]
  except:
    pass
  try:
    if data['movedn'] and position <= len(stops) - 2:
      stops[position + 1] = stops_copy[position]
      stops[position] = stops_copy[position + 1]
  except:
    pass
  tour.stops = ','.join(stops)
  tour.save()
  return redirect(f'/tours/{tour_id}/')



def tour_detail(request, tour_id):
    map_key = os.environ['MAP_KEY']
    # Get tour
    tour = Tour.objects.get(id=tour_id)
    stops = tour.stops.split(',')
    # Set tour start and finish and format for url
    origin = stops[0]
    destination = stops[len(stops) - 2]
    origin_formatted = stops[0].replace(' ', '+').replace('&', '+').replace('.', '')
    destination_formatted = stops[len(stops) - 2].replace(' ', '+').replace('&', '+').replace('.', '')
    # Assemble wineries in order for display on route
    waypoint_dicts = []
    for stop in stops:
      if len(stop):
        st = Winery.objects.get(name=stop)
        waypoint_dicts.append(st)
    # Assemble waypoints excluding first and last into list for url
    waypoints = list(tour.winery.all().exclude(Q(name=origin) | Q(name=destination)).values('name'))
    for idx, waypoint in enumerate(waypoints):
      waypoints[idx] = waypoint['name']

    # Format waypoints for url
    for idx in range(len(waypoints) - 1):
      waypoints[idx] = waypoints[idx] + '|'
    waypoint_concat = ''.join(waypoints).replace(' ', '+').replace('&', '+').replace('.', '')

    embed_url = (f'https://www.google.com/maps/embed/v1/directions?key={ map_key }&origin={ origin_formatted }&destination={ destination_formatted }&waypoints={ waypoint_concat }')
    return render(request, 'tour_detail.html', {
      'map_key': map_key,
      'tour': tour,
      'embed_url': embed_url,
      'waypoint_dicts': waypoint_dicts,
      })

def add_winery(request):
  data = request.POST.copy()
  winery = Winery.objects.get(id=int(data['winery']))
  if data['tour'] == 'create':
    user = User.objects.get(id=request.user.id)
    tour = Tour(name='Newly Created Tour', user=user)
    tour.save()
  else:
    tour = Tour.objects.get(id=int(data['tour']))
  tour.winery.add(winery)
  tour.stops += f'{winery},'
  tour.save()
  return redirect('/')

def search(request):
  return render(request,'search.html')

def serp(request):
  key = os.environ['MAP_KEY']
  google_places = GooglePlaces(key)
  regions = request.POST.getlist('region')
  print(regions)
  #query_result = google_places.nearby_search(location='Napa, California', keyword='Winery')
  if request.user.is_authenticated:
    tours = Tour.objects.filter(user=request.user.id)    
  else:
    tours = None
  query_result = Winery.objects.filter(region__in=regions)[:10]
  for query in query_result:
    call = google_places.text_search(query=query) 
    query.place_id = call._response['results'][0]['place_id']
    #query.image = call._response['results'][0]['photos'][0]['html_attributions']    
    query.rating = call._response['results'][0]['rating']
    #query.region = call._response['results'][0]['region']
    query.total_ratings = call._response['results'][0]['user_ratings_total']
    #query.open_now = call._response['results'][0]['opening_hours']['open_now']

  return render(request, 'serp.html', {'key': key, 'query_result': query_result, 'tours': tours})