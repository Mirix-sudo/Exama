from django.shortcuts import render
from .models import Epreuve
from django.db.models import Q
from django.http import JsonResponse

<<<<<<< HEAD
# Create your views here.
def home(request):
    return render(request, 'home.html')

=======
def home(request):
    epreuves_recentes = Epreuve.objects.order_by('-date_ajout')[:3]
    return render(request, "home.html", {'epreuve-recentes':epreuves_recentes})


def epreuve(request):
    epreuves=Epreuve.objects.all()

    #Recherche mot par mot-clé(titre, matire,et anné si un nom est taper)
    terme =request.GET.get('q','').strip()
    if terme:
        filter = Q(titre__icontains=terme) | Q(matiere__nom__icontains=terme)
        if terme.isdigit(): 
            filter |=Q(annee=int(terme))
        epreuves = epreuves.filter(filter)

        #filtrer
    matiere = request.GET.get('matiere')
    niveau = request.GET.get('niveau')
    annee = request.GET.get('annee')
    type_examen = request.GET.get('type_examen')
    section = request.GET.get('section')
    entite = request.GET.get('entite')

    if matiere:
        epreuves=epreuves.filter(matiere__nom = matiere)
    if niveau:
        epreuves=epreuves.filter(niveau=niveau)
    if annee:
        epreuves=epreuves.filter(annee=annee)
    if type_examen:
        epreuves=epreuves.filter(type_examen=type_examen)
    if section:
        epreuves=epreuves.filter(section=section)
    if entite:
        epreuves=epreuves.filter(entite=entite)

    return render(request, 'epreuves.html',{'epreuves':epreuves,'terme_rechercher':terme})

def recherche_ajax(request):
    terme = request.GET.get('q','')

    if len(terme) < 2:
        return JsonResponse({'resultats':[]})
    
    filter = Q(titre__icontains=terme) | Q(matier__nom__icontains=terme)
    if terme.isdigit():
        filter |=Q(annee=int(terme))

    epreuves =Epreuve.objects.filter(filter[:6])

    data = [
        {'id':e.id ,
        'titre':e.titre ,
        'matiere':e.matiere ,
        'niveau':e.niveau , 
        'annee':e.annee ,
        'url':f'/epreuves/{e.id}/' 
        }
        for e in epreuves
    ]
    return JsonResponse({'resultas':data})


def detail(request):
    return render(request, "epreuves_details.html")
>>>>>>> frontend

def home(request):
    return render(request, 'home.html')
def epreuves(request):
    return render(request, 'epreuves.html')
def epreuves_details(request):
    return render(request, 'epreuves_details.html')

