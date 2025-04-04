from django import forms
from django.contrib.auth import get_user_model  # Importez get_user_model
from .models import Note, Matiere

User = get_user_model()  # Utilisez get_user_model() pour obtenir le modèle utilisateur personnalisé

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['student', 'subject', 'value']

    student = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='Students'), label="Étudiant")
    subject = forms.ModelChoiceField(queryset=Matiere.objects.all(), label="Matière")
    value = forms.DecimalField(max_digits=5, decimal_places=2, label="Note")
