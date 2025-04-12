# PNEAPP/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import UserProfile
from django.contrib.auth import get_user_model

Utilisateur = get_user_model()

# Connexion
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Connexion réussie !")
            return redirect('dashboard')  # Redirige vers le dashboard ou une autre page
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    return render(request, "login.html")

# Inscription
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = form.cleaned_data['role']
            user.save()
            UserProfile.objects.create(user=user)  # Créer un profil utilisateur associé
            
            login(request, user)
            messages.success(request, "Inscription réussie ! Bienvenue sur la plateforme.")
            return redirect('dashboard')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})

# Déconnexion
def logout_view(request):
    logout(request)
    return redirect('login')

# PNEAPP/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Note, Matiere
from django.db.models import Avg

# Dashboard Utilisateur
@login_required
def dashboard(request):
    Utilisateur = get_user_model()  # Récupérer le modèle utilisateur personnalisé

    # Filtrer par rôle dans le modèle Utilisateur
    students_count = Utilisateur.objects.filter(role="etudiant").count()
    teachers_count = Utilisateur.objects.filter(role="prof").count()
    admins_count = Utilisateur.objects.filter(role="admin").count()

    return render(request, "dashboard.html", {
        "students_count": students_count,
        "teachers_count": teachers_count,
        "admins_count": admins_count,
    })

# Dashboard Admin
@login_required
def admin_dashboard(request):
    if request.user.role != 'admin':
        return redirect('login')  # Rediriger les utilisateurs non autorisés
    return render(request, 'admin_dashboard.html')

# Dashboard Professeur
@login_required
def professor_dashboard(request):
    if request.user.role != 'prof':
        return redirect('login')
    return render(request, 'professor_dashboard.html')

# Dashboard Étudiant
@login_required
def student_dashboard(request):
    if request.user.role != 'etudiant':
        return redirect('login')
    return render(request, 'student_dashboard.html')

# PNEAPP/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .forms import NoteForm
from .models import Note
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Ajouter une note
@login_required
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.etudiant = request.user
            note.save()
            messages.success(request, 'Note ajoutée avec succès!')
            return redirect('list_notes')
    else:
        form = NoteForm()
    notes = Note.objects.filter(etudiant=request.user)
    return render(request, 'notes/add_note.html', {'form': form, 'notes': notes})

# Lister les notes
@login_required
def list_notes(request):
    notes = Note.objects.filter(etudiant=request.user)
    return render(request, 'notes/list_notes.html', {'notes': notes})

# Mettre à jour une note
@login_required
def update_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, etudiant=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note mise à jour avec succès!')
            return redirect('list_notes')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/update_note.html', {'form': form, 'note': note})

# Supprimer une note
@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, etudiant=request.user)
    note.delete()
    messages.success(request, 'Note supprimée avec succès!')
    return redirect('list_notes')

# PNEAPP/views.py

import csv
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from .models import Note
from django.contrib.auth.decorators import login_required

# Exporter en CSV
@login_required
def export_csv(request):
    user = request.user
    if user.role == 'etudiant':
        notes = Note.objects.filter(etudiant=user)
    else:
        notes = Note.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=notes.csv'

    writer = csv.writer(response)
    writer.writerow(['Matière', 'Note', 'Mention'])

    for note in notes:
        writer.writerow([note.matiere.nom, note.note, note.mention])

    return response

# Exporter en PDF
@login_required
def export_pdf(request):
    user = request.user
    if user.role == 'etudiant':
        notes = Note.objects.filter(etudiant=user)
    else:
        notes = Note.objects.all()

    total_notes = sum(note.note for note in notes)
    moyenne = total_notes / len(notes) if notes else 0

    context = {
        'user': user,
        'notes': notes,
        'moyenne': moyenne,
    }

    html_content = render_to_string('bulletin.html', context)
    pdf = HTML(string=html_content).write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=bulletin.pdf'
    return response

# PNEAPP/views.py

from django.db.models import Avg
from .models import Note

def calculer_moyenne(user):
    notes = Note.objects.filter(etudiant=user)
    moyenne = notes.aggregate(Avg('note'))['note__avg']
    return moyenne

@login_required
def afficher_moyenne(request):
    if request.user.is_authenticated:
        moyenne = calculer_moyenne(request.user)
        notes = Note.objects.filter(etudiant=request.user)
        return render(request, 'moyenne.html', {'moyenne': moyenne, 'notes': notes})
    else:
        return redirect('login')

# PNEAPP/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .forms import MatiereForm
from .models import Matiere
from django.contrib.auth.decorators import login_required

# Liste des matières
@login_required
def list_matieres(request):
    matieres = Matiere.objects.all().distinct()  # Vous pouvez filtrer par rôle ou autre critère si nécessaire
    return render(request, 'matieres/list_matieres.html', {'matieres': matieres})

# Ajouter une matière
@login_required
def add_matiere(request):
    if request.method == 'POST':
        form = MatiereForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_matieres')
    else:
        form = MatiereForm()
    return render(request, 'matieres/add_matiere.html', {'form': form})

# Mettre à jour une matière
@login_required
def update_matiere(request, matiere_id):
    matiere = get_object_or_404(Matiere, id=matiere_id)
    if request.method == 'POST':
        form = MatiereForm(request.POST, instance=matiere)
        if form.is_valid():
            form.save()
            return redirect('list_matieres')
    else:
        form = MatiereForm(instance=matiere)
    return render(request, 'matieres/add_matiere.html', {'form': form})

# Supprimer une matière
@login_required
def delete_matiere(request, matiere_id):
    matiere = get_object_or_404(Matiere, id=matiere_id)
    if request.method == 'POST':
        matiere.delete()
        return redirect('list_matieres')
    return render(request, 'matieres/confirm_delete.html', {'matiere': matiere})
