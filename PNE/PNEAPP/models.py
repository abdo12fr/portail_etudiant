from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.db import models



class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=255, default='default_role')  # Valeur par défaut

    def __str__(self):
        return self.user.username


from django.contrib.auth.models import AbstractUser
from django.db import models

class Utilisateur(AbstractUser):
    role = models.CharField(
        max_length=50, 
        choices=[('etudiant', 'Étudiant'), ('prof', 'Professeur')], 
        default='etudiant'  # Ajoute une valeur par défaut
    )

    def __str__(self):
        return self.username

from django.db import models
from django.contrib.auth.models import User




from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description
