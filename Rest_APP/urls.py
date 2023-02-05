from django.contrib import admin # Taken from REST_API urls.py 
from django.urls import path  # Taken from REST_API urls.py

from .views import *

urlpatterns = [ # Taken from REST_API urls.py
    path("", home), # Taken from REST_API urls.py
] # Taken from REST_API urls.py