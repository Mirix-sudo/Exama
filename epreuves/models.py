from django.db import models
from django.utils import choices



class Epreuve(models.Model):
    ENTITES = [
       ("FAST", "FAST"),
       ("ENS", "ENS"),
    ]
    NIVEAUX = [
        ('1', '1ère année'),
        ('2', '2ème année'),
        ('3', '3ème année'),
    ]
    SESSION = [
        ('Examen', 'Examen Final'),
        ('Rattrapage', 'Rattrapage'),
    ]
    entite = models.CharField(max_length=100, default=ENTITES[0][0], choices=ENTITES)
    niveau = models.CharField(max_length=100, default="Choisissez votre niveau", choices=NIVEAUX)
    annee = models.IntegerField()
    session = models.CharField(max_length=100, default="Quel est la session?" ,choices=SESSION)
    fichier = models.FileField(upload_to='epreuves/')
    matiere = models.ForeignKey('Matiere', on_delete=models.CASCADE, related_name='epreuves')
    date_ajout = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.entite} - {self.matiere} - {self.niveau} - {self.annee} - {self.session}"

class Matiere(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nom