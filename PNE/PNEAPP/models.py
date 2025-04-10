# PNEAPP/models.py
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractUser
from django.db import models

class Utilisateur(AbstractUser):
    role = models.CharField(
        max_length=50,
        choices=[('etudiant', 'Étudiant'), ('prof', 'Professeur')],
        default='etudiant'
    )


# Ajoutez ce modèle UserProfile
class UserProfile(models.Model):
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='profile')
    matricule = models.CharField(max_length=20, blank=True, null=True)
    classe = models.CharField(max_length=50, blank=True, null=True)
    ecole = models.CharField(max_length=100, blank=True, null=True)
    groupe = models.CharField(max_length=50, blank=True, null=True)
    numerocne = models.CharField(max_length=20, blank=True, null=True)
    sexe = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Féminin')], blank=True, null=True)
    date_naissance = models.DateField(blank=True, null=True)
    nationalite = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return f"Profil de {self.user.username}"


# Modèle Image (si vous voulez gérer des images dans votre projet)
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

from django.db import models
from django.conf import settings

class Matiere(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

from django.utils import timezone

class Note(models.Model):
    MENTION_CHOICES = [
        ('TB', 'Très Bien'),
        ('B', 'Bien'),
        ('AB', 'Assez Bien'),
        ('P', 'Passable'),
        ('I', 'Insuffisant'),
    ]

    matricule = models.CharField(max_length=50, unique=True, default="UNKNOWN")
    etudiant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    note = models.FloatField()
    mention = models.CharField(max_length=50, choices=MENTION_CHOICES)
    date_saisie = models.DateTimeField(auto_now_add=True)  # Retiré le `default`

    def __str__(self):
        return f"Note de {self.etudiant} en {self.matiere}"

