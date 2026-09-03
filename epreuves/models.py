from django.db import models
from django.utils import choices

# Create your models here.


class Epreuve(models.Model):
    ENTITES = [
       ("FAST", "FAST"),
       ("FST", "FST"),
    ]
    NIVEAUX = [
        ('1', '1ère année'),
        ('2', '2ème année'),
        ('3', '3ème année'),
    ]
    TYPES_EXAMEN = [
        ('CC', 'Contrôle Continu'),
        ('EX', 'Examen Final'),
    ]
    entite = models.CharField(max_length=100, default=ENTITES[0][0], choices=ENTITES)
    niveau = models.CharField(max_length=100, choices=NIVEAUX)
    annee = models.IntegerField()
    type_examen = models.CharField(max_length=100, choices=TYPES_EXAMEN)
    fichier = models.FileField(upload_to='epreuves/')
    matiere = models.ForeignKey('Matiere', on_delete=models.PROTECT)
    date_ajout = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.entite} - {self.matiere} - {self.niveau} - {self.annee} - {self.type_examen}"

class Matiere(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nom