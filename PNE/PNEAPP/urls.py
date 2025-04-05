from django import views
from django.urls import path
from .views import CustomLoginView
from .views import (
    login_view,
    logout_view,
    profile_view,
    dashboard,
    accueil_utilisateur,
    register,
    add_note,
    delete_note,
    update_note,
    list_notes,
)

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path("profile/", profile_view, name="profile"),
    path("dashboard/", dashboard, name="dashboard"),
    path("register/", register, name="register"),
    path('accueil/', accueil_utilisateur, name='accueil'),
    path("logout/", logout_view, name="logout"),
    path('notes/', list_notes, name='list_notes'),
    path('notes/add/', add_note, name='add_note'),
    path('notes/update/<int:note_id>/', update_note, name='update_note'),
    path('notes/delete/<int:note_id>/', delete_note, name='delete_note'),
]
