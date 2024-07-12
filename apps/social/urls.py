from django.urls import path

from apps.social.views import login_view, signup_view, logout_view, settings_view

urlpatterns = [
    path("login", login_view, name="login"),
    path("signup", signup_view, name="signup"),
    path("logout", logout_view, name="logout"),
    path("settings", settings_view, name="settings")
]
