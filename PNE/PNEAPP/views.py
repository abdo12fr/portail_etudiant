from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages




from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Connexion réussie !")
            return redirect("dashboard")  # Assure-toi que cette route existe dans urls.py
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")

    return render(request, "login.html")



from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import UserProfile  # Si tu as un modèle de profil pour stocker des informations supplémentaires



from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Sauvegarde de l'utilisateur
            user = form.save()

            # Connexion automatique de l'utilisateur après l'inscription
            login(request, user)

            # Ajout d'un message de succès
            messages.success(request, 'Votre inscription a été réussie ! Vous êtes maintenant connecté.')

            # Redirection vers la page de connexion ou tableau de bord
            return redirect('dashboard')  # Assurez-vous que vous avez une page de dashboard ou connexion
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})





def dashboard(request):
    students_count = UserProfile.objects.filter(role="student").count()
    teachers_count = UserProfile.objects.filter(role="teacher").count()
    admins_count = UserProfile.objects.filter(role="admin").count()

    return render(request, "dashboard.html", {
        "students_count": students_count,
        "teachers_count": teachers_count,
        "admins_count": admins_count,
    })

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


 
from django.shortcuts import render

def profile_view(request):
    return render(request, "profile.html")

from django.http import JsonResponse

def hello_world(request):
    return JsonResponse({"message": "Hello from Django API!"})





