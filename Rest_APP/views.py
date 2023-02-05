from django.shortcuts import render
from rest_framework.decorators import api_view #***
from rest_framework.response import Response #***
@api_view() #***
# Create your views here.

def home(request): #***
    return Response({'status':200,"message":"This Is First Rest api Project"}) #***