from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Epreuve, Matiere
from django.db.models import Q

def home(request):
    epreuves_recentes = Epreuve.objects.order_by('-date_ajout')[:3]
    return render(request, "home.html", {'epreuves_recentes': epreuves_recentes})


# def epreuves(request):
#     epreuves=Epreuve.objects.all()

#     # Recherche par matière ou année.
#     terme =request.GET.get('q','').strip()
#     if terme:
#         filtre = Q(matiere__nom__icontains=terme)
#         if terme.isdigit(): 
#             filtre |= Q(annee=int(terme))
#         epreuves = epreuves.filter(filtre)

#         #filtrer
#     matiere = request.GET.get('matiere', '').strip()
#     niveau = request.GET.get('niveau')
#     annee = request.GET.get('annee', '').strip()
#     entite = request.GET.get('entite')

#     if matiere:
#         epreuves = epreuves.filter(matiere__nom=matiere)
#     if niveau:
#         epreuves=epreuves.filter(niveau=niveau)
#     if annee:
#         epreuves=epreuves.filter(annee=annee)
#     if entite:
#         epreuves=epreuves.filter(entite=entite)

#     return render(request, 'epreuves.html', {
#         'epreuves': epreuves,
#         'matiere_recherchee': matiere,
#         'annee_recherchee': annee,
#         'matieres': Matiere.objects.order_by('nom'),
#         'annees': Epreuve.objects.order_by('-annee').values_list('annee', flat=True).distinct(),
#     })
def liste_epreuves(request):

    epreuves = Epreuve.objects.all()

    matiere = request.GET.get("matiere")
    niveau = request.GET.get('niveau')
    annee = request.GET.get('annee', '').strip()
    entite = request.GET.get('entite')

    if matiere:
        epreuves = epreuves.filter(matiere_id=matiere)

    if niveau:
        epreuves = epreuves.filter(niveau=niveau)

    if annee:
        epreuves = epreuves.filter(annee=annee)
    if entite:
        epreuves = epreuves.filter(entite=entite)

    return render(request, "epreuves.html", {
        "epreuves": epreuves,
        "matieres": Matiere.objects.order_by("nom"),
        "annees": Epreuve.objects.order_by("-annee").values_list("annee", flat=True).distinct(),
        "matiere_recherchee": matiere,
        "annee_recherchee": annee,
    })


def epreuves_details(request, id):
    epreuve = get_object_or_404(Epreuve, id=id)
    return render(request, "epreuves_details.html", {
        "epreuve": epreuve,
    })

# URL pattern for the details view
# path("epreuves/<int:id>/", views.epreuves_details, name="epreuves_details")

