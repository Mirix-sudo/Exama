from django.db import models

# Create your models here.


class Epreuve(models.Model):
    NIVEAUX = [
        ('1', '1ère année'),
        ('2', '2ème année'),
        ('3', '3ème année'),
    ]
    TYPES_EXAMEN = [
        ('CC', 'Contrôle Continu'),
        ('EX', 'Examen Final'),
    ]
    titre = models.CharField(max_length=100)
    matiere = models.CharField(max_length=100)
    niveau = models.CharField(max_length=100, choices=NIVEAUX)
    annee = models.IntegerField()
    type_examen = models.CharField(max_length=100, choices=TYPES_EXAMEN)
    fichier = models.FileField(upload_to='epreuves/')
    matiere = models.ForeignKey('Matiere', on_delete=models.PROTECT)
    date_ajout = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.titre

class Matiere(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nom