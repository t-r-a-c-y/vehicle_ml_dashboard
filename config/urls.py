# config/urls.py 
from django.urls import path, include 
urlpatterns = [ 
path("", include("vehicles.urls")), 
] 