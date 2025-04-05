from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, NoteForm
from .models import UserProfile, Note

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

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Créer l'utilisateur mais ne pas encore sauvegarder
            user = form.save(commit=False)
            # Définir le rôle à partir du formulaire
            user.role = form.cleaned_data['role']
            # Maintenant sauvegarder l'utilisateur
            user.save()
            
            # Créer un profil utilisateur associé
            UserProfile.objects.create(
                user=user,
                # Vous pouvez ajouter d'autres champs ici si nécessaire
            )
            
            # Connecter l'utilisateur
            login(request, user)
            messages.success(request, "Inscription réussie ! Bienvenue sur la plateforme.")
            return redirect('dashboard')
        else:
            # Si le formulaire n'est pas valide, afficher les erreurs
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

from django.contrib.auth import get_user_model

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


# Profil utilisateur
@login_required
def profile_view(request):
    return render(request, "profile.html")

# Accueil utilisateur
@login_required
def accueil_utilisateur(request):
    return render(request, 'accueil.html')


# PNEAPP/views.py





from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Note, Matiere
from django.contrib import messages

def add_note(request):
    if request.method == 'POST':
        # Ici, on crée le formulaire en utilisant les données de la requête POST
        form = NoteForm(request.POST)
        if form.is_valid():
            # Si le formulaire est valide, on l'enregistre dans la base de données
            form.save()
            messages.success(request, "Note ajoutée avec succès !")
            return redirect('add_note')  # Rediriger vers la même page pour afficher la note
    else:
        form = NoteForm()

    # Passer le formulaire au template
    return render(request, 'notes/add_note.html', {'form': form})



@login_required
def list_notes(request):
    notes = Note.objects.all()
    return render(request, 'notes/list_notes.html', {'notes': notes})

@login_required
def update_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('list_notes')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/update_note.html', {'form': form})

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('list_notes')
    return render(request, 'notes/delete_note.html', {'note': note})

# views.py
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    def get_success_url(self):
        user = self.request.user
        if user.role == 'prof':
            return '/notes/add/'
        elif user.role == 'etudiant':
            return '/profile/'
        else:
            return 'accueil'  # page d'accueil par défaut
