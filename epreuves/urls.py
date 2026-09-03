from django.urls import path 
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('epreuve/', views.epreuve, name='epreuve'),
    path('detail/', views.detail, name='detail'),
    path('recherches/', views.recherche_ajax, name='recherches')
    ]

