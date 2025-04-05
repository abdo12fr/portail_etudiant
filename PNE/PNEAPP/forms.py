# PNEAPP/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Matiere, Utilisateur, Note

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(
        choices=[('etudiant', 'Étudiant'), ('prof', 'Professeur'), ('admin', 'Administrateur')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'password1', 'password2', 'role']



from django import forms
from .models import Note, Matiere
from django.contrib.auth import get_user_model

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['etudiant', 'matiere', 'note', 'mention']
        widgets = {
            'note': forms.NumberInput(attrs={'min': 0, 'max': 20}),
        }

    # Ajouter un champ personnalisé pour le prénom et le nom de l'étudiant
    # Assumer que le modèle Note a une relation avec l'utilisateur (étudiant)
    # Ici, on va récupérer l'utilisateur connecté et l'associer à la note
    nom_prenom = forms.CharField(label="Nom et Prénom de l'élève", max_length=100, required=True)
