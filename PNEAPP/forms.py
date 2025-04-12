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



# PNEAPP/forms.py
from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['matiere', 'note', 'mention']
        widgets = {
            'matiere': forms.Select(attrs={'class': 'form-control'}),
            'note': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '20'}),
            'mention': forms.Select(attrs={'class': 'form-control'}),
        }


from django import forms
from .models import Matiere
from django.core.exceptions import ValidationError

class MatiereForm(forms.ModelForm):
    class Meta:
        model = Matiere
        fields = ['nom']

    def clean_nom(self):
        nom = self.cleaned_data['nom']
        if Matiere.objects.filter(nom__iexact=nom).exists():
            raise ValidationError("Cette matière existe déjà.")
        return nom
