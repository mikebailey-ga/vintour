from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from googleplaces import GooglePlaces, types, lang
import os
from .models import Winery, Tour, User
from django.db.models import Q


query_result_raw = Winery.objects.all()
for query in query_result_raw:
  print(query)
  call = google_places.text_search(query=query) 
  if(call.has_attributions):    
    query.rating = call._response['results'][0]['rating']
    if float(query.rating) > 0:
      query.save()
      