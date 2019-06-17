from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from googleplaces import GooglePlaces, types, lang
import os
from .models import Winery

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

def map(request):
    map_key = os.environ['MAP_KEY']
    return render(request, 'mapembed.html', {'map_key': map_key})

def serp(request):
  key = os.environ['MAP_KEY']
  #google_places = GooglePlaces(key)
  #query_result = google_places.nearby_search(location='Napa, California', keyword='Winery')

  query_result = Winery.objects.all()

  return render(request, 'serp.html', {'key': key, 'query_result': query_result})