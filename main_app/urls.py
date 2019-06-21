from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tours/<int:tour_id>/', views.tour_detail, name='tour_detail'),
    path('tours/<int:pk>/delete/', views.TourDelete.as_view(), name='tour_delete'),
    path('tours/<int:tour_id>/name_tour/', views.name_tour, name='name_tour'),
    path('tours/<int:tour_id>/reorder/', views.stop_reorder, name='stop_reorder'),
    path('tours/<int:tour_id>/unassoc_winery/<int:winery_id>/', views.unassoc_winery, name='unassoc_winery'),
    path('accounts/signup/', views.signup, name='signup'),
    path('search/', views.search, name='search'),
    path('serp/', views.serp, name='serp'),
    path('profile/', views.profile, name='profile'),
    path('recommendedtrips/', views.recommendedtrips, name='recommendedtrips'),
    path('tours/add/', views.add_winery, name='add_winery'),
    path('dbupdate/', views.dbupdate, name='dbupdate'),
]