from django.shortcuts import render
from views import epreuves, epreuves_details, home

# Create your views here.

def home(request):
    return render(request, 'home.html')

def epreuves(request):
    return render(request, 'epreuves.html')

def epreuves_details(request):
    return render(request, 'epreuves_details.html')