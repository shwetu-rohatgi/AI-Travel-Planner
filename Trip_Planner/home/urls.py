from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home-homepage"), #empty string to keep it as home landing page 
    path('search/', views.search, name = "home-search")
]