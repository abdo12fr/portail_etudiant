from django.contrib import admin
from .models import Utilisateur, Matiere, Note

admin.site.register(Utilisateur)
admin.site.register(Matiere)
admin.site.register(Note)
