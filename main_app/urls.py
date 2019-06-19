from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('search/', views.search, name='search'),
    path('serp/', views.serp, name='serp'),
    path('profile/', views.profile, name='profile'),
    path('recommendedtrips/', views.recommendedtrips, name='recommendedtrips'),
    path('tours/add/', views.add_winery, name='add_winery'),
]