from django import views
from django.urls import path
<<<<<<< HEAD
from .views import CustomLoginView, add_matiere, admin_dashboard, afficher_moyenne, bulletin, delete_matiere, list_matieres, professor_notes, update_matiere
from .views import (
    login_view,
=======
from .views import CustomLoginView, add_matiere, dashboard_professeur, dashboard_student, delete_matiere, export_bulletin_pdf, import_notes_excel, list_matieres, unauthorized_access, update_matiere
from .views import (
>>>>>>> 912d90e (Initial commit)
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
<<<<<<< HEAD
    path('notes/prof/', professor_notes, name='notes_prof'),
=======
>>>>>>> 912d90e (Initial commit)
    path('matieres/add/',add_matiere, name='add_matiere'),
    path('matieres/', list_matieres, name='list_matieres'),
    path('matieres/modifier/<int:matiere_id>/', update_matiere, name='update_matiere'),
    path('matieres/supprimer/<int:matiere_id>/', delete_matiere, name='delete_matiere'),
<<<<<<< HEAD
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

=======
    path('notes/export/pdf/', export_bulletin_pdf, name='export_bulletin_pdf'),
    path('notes/import/', import_notes_excel, name='import_notes_excel'),
    path('dashboard/etudiant/', dashboard_student, name='dashboard_student'),
    path("dashboard/professeur/", dashboard_professeur, name="dashboard_professeur"),
    path('access-denied/', unauthorized_access, name='access_denied'),
]





>>>>>>> 912d90e (Initial commit)
