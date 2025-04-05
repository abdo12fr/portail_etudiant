# PNEAPP/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur, Note

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
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['etudiant', 'matiere', 'note', 'mention']
