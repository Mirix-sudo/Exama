from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')
def epreuves(request):
    return render(request, 'epreuves.html')
def epreuves_details(request):
    return render(request, 'epreuves_details.html')