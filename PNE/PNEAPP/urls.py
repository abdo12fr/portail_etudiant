from django import views
from django.urls import path
from .views import  login_view, profile_view, dashboard, register_view  # Vérifie que profile_view est bien ici


urlpatterns = [
    path("", login_view, name="login"),
    path("profile/", profile_view, name="profile"),
    path("dashboard/", dashboard, name="dashboard"),
    path("register/", register_view, name="register"),

]





