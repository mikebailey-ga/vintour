from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    bio = models.TextField()

class Winery(models.Model): 
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True, default='')
    desc = models.CharField(max_length=1000, blank=True, default='')
    price = models.CharField(max_length=50, blank=True, default='')
    rating = models.CharField(max_length=10, blank=True, default='')
    region = models.CharField(max_length=50, blank=True, default='')
<<<<<<< HEAD
    grapes = models.CharField(max_length=500, blank=True)
=======
    grapes = models.CharField(max_length=1000, blank=True)
>>>>>>> d4df817328f8625525cd1028c9416e4a29316fb7

    def __str__(self):
        return self.name

class Tour(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, default='Newly Created Tour')
    regions = models.CharField(max_length=250, blank=True)
    winery = models.ManyToManyField(Winery)
    stops = models.CharField(max_length=300, blank=True)    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tour_detail', kwargs={'pk': self.id})