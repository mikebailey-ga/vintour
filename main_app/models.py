from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    bio = models.TextField()

class Tour(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    numberofstops = models.IntegerField()
    traveldistance = models.FloatField()
    traveltime = models.FloatField()
    regions = models.CharField(max_length=250)

class Stop(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    region = models.CharField(max_length=50)
    hoursopen = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)

class Winery(models.Model): 
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    website = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    cave = models.BooleanField(blank=True)
    tours = models.BooleanField(blank=True)
    notes = models.CharField(max_length=200, blank=True)
    
