from django.urls import path 
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('epreuves/', views.epreuves, name='epreuves'),
    path('epreuves/<int:id>/', views.epreuves_details, name='epreuves_details'),
]
