import requests
import firebase_admin
from django.shortcuts import render
from firebase_admin import credentials, firestore

from djangoProject.forms import HomeForm


cred = credentials.Certificate('./firebase_credentials.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()
# Create your views here.

def home_view(request):
    if request.method == 'POST':
        context = {'room': request.POST.get('room')}
        return render(request, 'rooms/main.html', context)
    else:
        return render(request, 'home/home.html')
