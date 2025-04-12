from django import views
from django.urls import path
from .views import CustomLoginView, add_matiere, admin_dashboard, afficher_moyenne, bulletin, delete_matiere, list_matieres, professor_notes, update_matiere
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
    path('notes/prof/', professor_notes, name='notes_prof'),
    path('matieres/add/',add_matiere, name='add_matiere'),
    path('matieres/', list_matieres, name='list_matieres'),
    path('matieres/modifier/<int:matiere_id>/', update_matiere, name='update_matiere'),
    path('matieres/supprimer/<int:matiere_id>/', delete_matiere, name='delete_matiere'),
    path('moyenne/', afficher_moyenne, name='afficher_moyenne'),
    path('bulletin/', bulletin, name='bulletin'),  # Page du bulletin
    path('dashboard/', views.home, name='home'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
    path('dashboard/student/report/', views.student_report, name='student_report'),
    path('dashboard/professor/', views.professor_dashboard, name='professor_dashboard'),
    path('dashboard/professor/notes/', views.professor_notes, name='professor_notes'),
    path('student/report/pdf/', views.export_pdf, name='export_pdf'),
    path('student/report/csv/', views.export_csv, name='export_csv'),
    path('student/report/excel/', views.export_excel, name='export_excel'),


]

