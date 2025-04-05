
# PNEAPP/apps.py
from django.apps import AppConfig

class PneappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PNEAPP'
    
    def ready(self):
        import PNEAPP.signals  # Importez les signaux ici