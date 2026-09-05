import unicodedata

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404

from .models import Epreuve, Matiere


def _normaliser_recherche(valeur):
    valeur = unicodedata.normalize("NFKD", str(valeur))
    return "".join(
        caractere
        for caractere in valeur
        if not unicodedata.combining(caractere)
    ).casefold()


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

    # Filtres
    recherche = request.GET.get("q", "").strip()
    matiere = request.GET.get("matiere", "").strip()
    niveau = request.GET.get("niveau", "").strip()
    session = request.GET.get("session", "").strip()
    annee = request.GET.get("annee", "").strip()
    entite = request.GET.get("entite", "").strip()


    if matiere:
        epreuves = epreuves.filter(matiere_id=matiere)

    if niveau:
        epreuves = epreuves.filter(niveau=niveau)

    if session:
        epreuves = epreuves.filter(session=session)

    if annee:
        epreuves = epreuves.filter(annee=annee)

    if entite:
        epreuves = epreuves.filter(entite=entite)

    if recherche:
        terme = _normaliser_recherche(recherche)
        epreuves = [
            epreuve
            for epreuve in epreuves
            if any(
                terme in _normaliser_recherche(valeur)
                for valeur in (
                    epreuve.matiere.nom,
                    epreuve.get_niveau_display(),
                    epreuve.get_session_display(),
                    epreuve.entite,
                    epreuve.get_entite_display(),
                    str(epreuve.annee),
                )
            )
        ]


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

        "sessions": Epreuve.SESSION,

        "recherche": recherche,

        "matiere_recherchee": matiere,

        "niveau_recherche": niveau,

        "session_recherchee": session,

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


def login_view(request):

    if request.user.is_authenticated:
        return redirect("home")

    erreur = None

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        utilisateur = authenticate(
            request,
            username=username,
            password=password,
        )

        if utilisateur is not None:
            login(request, utilisateur)
            return redirect("home")

        erreur = "Nom d'utilisateur ou mot de passe incorrect."

    return render(request, "login.html", {"erreur": erreur})


def logout_view(request):
    if request.method == "POST":
        logout(request)

    return redirect("login")