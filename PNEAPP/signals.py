# PNEAPP/signals.py (créez ce fichier)
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Utilisateur, UserProfile

@receiver(post_save, sender=Utilisateur)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

<<<<<<< HEAD
@receiver(post_save, sender=Utilisateur)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
=======
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=Utilisateur)
def save_user_profile(sender, instance, created, **kwargs):
    # Vérifie si un profil existe déjà pour l'utilisateur
    if created:
        # Si l'utilisateur est créé, créer un profil associé
        UserProfile.objects.create(user=instance)
    else:
        # Si l'utilisateur existe déjà, vérifie si son profil existe
        if not hasattr(instance, 'profile'):
            UserProfile.objects.create(user=instance)
    
    # Sauvegarder le profil de l'utilisateur
    instance.profile.save()


from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Utilisateur

@receiver(post_save, sender=Utilisateur)
def set_default_role(sender, instance, created, **kwargs):
    if created and not instance.role:
        instance.role = 'etudiant'
        instance.save()
>>>>>>> 912d90e (Initial commit)
