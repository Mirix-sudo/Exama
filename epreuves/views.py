from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Epreuve, Matiere


def home(request):

    epreuves_recentes = (
        Epreuve.objects
        .select_related("matiere")
        .order_by("-date_ajout")[:3]
    )

    return render(request, "home.html", {
        "epreuves_recentes": epreuves_recentes,
    })


def liste_epreuves(request):

    epreuves = Epreuve.objects.select_related("matiere")

    # Recherche
    recherche = request.GET.get("q", "").strip()

    if recherche:

        filtre = Q(matiere__nom__icontains=recherche)

        if recherche.isdigit():
            filtre |= Q(annee=int(recherche))

        epreuves = epreuves.filter(filtre)


    # Filtres
    matiere = request.GET.get("matiere", "").strip()
    niveau = request.GET.get("niveau", "").strip()
    annee = request.GET.get("annee", "").strip()
    entite = request.GET.get("entite", "").strip()


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

        "annees": (
            Epreuve.objects
            .order_by("-annee")
            .values_list("annee", flat=True)
            .distinct()
        ),

        "niveaux": Epreuve.NIVEAUX,

        "recherche": recherche,

        "matiere_recherchee": matiere,

        "niveau_recherche": niveau,

        "annee_recherchee": annee,

    })


def epreuves_details(request, id):

    epreuve = get_object_or_404(
        Epreuve.objects.select_related("matiere"),
        id=id
    )

    return render(request, "epreuves_details.html", {
        "epreuve": epreuve,
    })