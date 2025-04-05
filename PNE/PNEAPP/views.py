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



from .models import Note
from .forms import NoteForm
from django.contrib.auth.decorators import login_required

@login_required
def liste_notes(request):
    notes = Note.objects.all()
    return render(request, 'notes/liste_notes.html', {'notes': notes})

@login_required
def ajouter_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_notes')
    else:
        form = NoteForm()
    return render(request, 'notes/ajouter_note.html', {'form': form})

@login_required
def modifier_note(request, pk):  # Utilisation du paramètre pk
    note = get_object_or_404(Note, pk=pk)  # Cherche la note par pk
    form = NoteForm(request.POST or None, instance=note)
    
    if form.is_valid():
        form.save()
        return redirect('liste_notes')
    
    return render(request, 'notes/modifier_note.html', {'form': form})




@login_required
def supprimer_note(request):
    pk = request.GET.get('id')
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('liste_notes')
    return render(request, 'notes/supprimer_note.html', {'note': note})
