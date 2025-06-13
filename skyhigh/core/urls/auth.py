# core/urls/auth.py
from django.urls import path
from django.contrib.auth import views as auth_views
from core.views.auth import signup_view, profile_view

app_name = 'auth'  # ✅ This is required for namespacing

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', signup_view, name='signup'),
    path('profile/', profile_view, name='profile'),
]
