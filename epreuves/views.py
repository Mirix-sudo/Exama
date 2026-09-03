from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Epreuve
from django.db.models import Q
from django.http import JsonResponse

def home(request):
    epreuves_recentes = Epreuve.objects.order_by('-date_ajout')[:3]
    return render(request, "home.html", {'epreuves_recentes': epreuves_recentes})


def epreuves(request):
    epreuves=Epreuve.objects.all()

    # Recherche par matière ou année.
    terme =request.GET.get('q','').strip()
    if terme:
        filtre = Q(matiere__nom__icontains=terme)
        if terme.isdigit(): 
            filtre |= Q(annee=int(terme))
        epreuves = epreuves.filter(filtre)

        #filtrer
    matiere = request.GET.get('matiere')
    niveau = request.GET.get('niveau')
    annee = request.GET.get('annee')
    entite = request.GET.get('entite')

    if matiere:
        epreuves = epreuves.filter(matiere__nom=matiere)
    if niveau:
        epreuves=epreuves.filter(niveau=niveau)
    if annee:
        epreuves=epreuves.filter(annee=annee)
    if entite:
        epreuves=epreuves.filter(entite=entite)

    return render(request, 'epreuves.html',{'epreuves':epreuves,'terme_rechercher':terme})

def recherche_ajax(request):
    terme = request.GET.get('q','')

    if len(terme) < 2:
        return JsonResponse({'resultats':[]})
    
    filtre = Q(matiere__nom__icontains=terme)
    if terme.isdigit():
        filtre |= Q(annee=int(terme))

    epreuves = Epreuve.objects.filter(filtre)[:6]

    data = [
        {'id': e.id,
        'matiere': str(e.matiere),
        'niveau': e.niveau,
        'annee': e.annee,
        'url': f'/epreuves/{e.id}/'
        }
        for e in epreuves
    ]
    return JsonResponse({'resultats': data})

from django.shortcuts import get_object_or_404

def epreuves_details(request, id):
    epreuve = get_object_or_404(Epreuve, id=id)
    return render(request, "epreuves_details.html", {
        "epreuve": epreuve,
    })

# URL pattern for the details view
# path("epreuves/<int:id>/", views.epreuves_details, name="epreuves_details")

