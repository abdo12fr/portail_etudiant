from django.urls import path
from .views import (
    login_view,
    logout_view,
    profile_view,
    dashboard,
    accueil_utilisateur,
    register,
    liste_notes,
    ajouter_note,
    modifier_note,
    supprimer_note,
)

urlpatterns = [
    path("", login_view, name="login"),
    path("profile/", profile_view, name="profile"),
    path("dashboard/", dashboard, name="dashboard"),
    path("register/", register, name="register"),
    path("accueil/", accueil_utilisateur, name="accueil_utilisateur"),
    path("logout/", logout_view, name="logout"),
    path('notes/', liste_notes, name='liste_notes'),
    path('notes/ajouter/', ajouter_note, name='ajouter_note'),
    path('notes/modifier/', modifier_note, name='modifier_note'),
    path('notes/supprimer/', supprimer_note, name='supprimer_note'),

]
