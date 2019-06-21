from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
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
    # request.session.flush()
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

@login_required
def profile(request):
    tours = Tour.objects.filter(user=request.user.id)
    return render (request, 'profile.html', {'tours': tours})

def recommendedtrips(request):
    return render(request, 'recommended-trips.html')

@login_required
def stop_reorder(request, tour_id):
  # Get req data and tour in question
  data = request.POST.copy()
  tour = Tour.objects.get(id=tour_id)
  # Get stop's position along tour and listify stops for reordering
  position = int(data['position'])
  stops = list(filter(None, tour.stops.split(',')))
  stops_copy = stops.copy()
  # If up arrow is pressed, winery is swapped with the one preceding it
  try:
    if data['moveup'] and position >= 1:
      stops[position - 1] = stops[position]
      stops[position] = stops_copy[position - 1]
  except:
    pass
  # If down arrow is pressed, winery is swapped with winery after it on route
  try:
    if data['movedn'] and position <= len(stops) - 2:
      stops[position + 1] = stops_copy[position]
      stops[position] = stops_copy[position + 1]
  except:
    pass
  # Stop string reassembled for storage in db and saved
  tour.stops = f'{",".join(stops)},'
  tour.save()
  return redirect(f'/tours/{tour_id}/')


@login_required
def tour_detail(request, tour_id):
  map_key = os.environ['MAP_KEY']
  # Get tour
  tour = Tour.objects.get(id=tour_id)
  stops = tour.stops.split(',')
  # Set tour start and finish and format for url
  origin = stops[0].replace(' ', '+').replace('&', '+').replace('.', '')
  destination = stops[len(stops) - 2].replace(' ', '+').replace('&', '+').replace('.', '')
  # Assemble wineries in order for display on route
  waypoint_dicts = []
  for stop in stops:
    if len(stop):
      st = Winery.objects.get(name=stop)
      waypoint_dicts.append(st)
  # Assemble waypoints excluding first and last into list for url
  waypoints = stops[1:-1]
  # Format waypoints for url
  for idx in range(len(waypoints) - 1):
    waypoints[idx] = waypoints[idx] + '|'
  waypoint_concat = ''.join(waypoints).replace(' ', '+').replace('&', '+').replace('.', '')
  # Displays map with single marker if only one stop added to tour
  if len(stops) <= 2:
    embed_url = f'https://www.google.com/maps/embed/v1/place?q={origin}&key={ map_key }'
  else:
    embed_url = (f'https://www.google.com/maps/embed/v1/directions?key={ map_key }&origin={ origin }&destination={ destination }&waypoints={ waypoint_concat }')
  return render(request, 'tour_detail.html', {
    'map_key': map_key,
    'tour': tour,
    'embed_url': embed_url,
    'waypoint_dicts': waypoint_dicts,
    })

@login_required
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
  return redirect('/tours/' + str(tour.id) + '/')

@login_required
def name_tour(request, tour_id):
  tour = Tour.objects.get(id=tour_id)
  tour.name = request.POST['name']
  tour.save()
  return redirect('tour_detail', tour_id=tour_id)

class TourDelete(LoginRequiredMixin, DeleteView):
  model = Tour
  success_url = '/profile/'

@login_required
def unassoc_winery(request, tour_id, winery_id):
  tour = Tour.objects.get(id=tour_id)
  tour.winery.remove(winery_id)
  tour.stops = tour.stops.replace(f'{Winery.objects.get(id=winery_id).name},', '')
  tour.save()
  return redirect('tour_detail', tour_id=tour_id)

def search(request):
  return render(request,'search.html')

@login_required
def serp(request):
  key = os.environ['MAP_KEY']
## Keeps the search settings in sessions for pagination.
  if 'regions' in request.session:
    regions = request.session['regions']
  else:
    regions = request.POST.getlist('region')
    request.session['regions'] = regions
  if 'grape' in request.session:
    grapes = request.session['grape']
  else:
    grapes = request.POST.getlist('grape')
    request.session['grape'] = grapes

  if request.user.is_authenticated:
    tours = Tour.objects.filter(user=request.user.id)    
  else:
    tours = None

## If the user doesn't check anything, it defaults to all. Probably a better way to do this
  if len(regions) == 0:
    regions = ['Napa', 'Sonoma']

  if len(grapes) == 0:
    query_result_raw = Winery.objects.filter(region__in=regions).order_by('name')[:20]
  
  else:
    print(grapes[0])
    query_result_raw = Winery.objects.filter(Q(region__in=regions) & Q(grapes__icontains=grapes[0])).order_by('name')

  page = request.GET.get('page', 1)
  paginator = Paginator(query_result_raw, 20)
  query_result = paginator.get_page(page)
  return render(request, 'serp.html', {'key': key, 'query_result': query_result, 'tours': tours})

  
def dbupdate(request):
  key = os.environ['MAP_KEY']
  google_places = GooglePlaces(key)  
  query_result_raw = Winery.objects.all()
  for query in query_result_raw:
    print(query)
    call = google_places.text_search(query=query) 
    if(call.has_attributions):    
      query.rating = call._response['results'][0]['rating']
      if float(query.rating) > 0:
        query.save()
        