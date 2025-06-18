# core/urls/auth.py

from core.views.auth import profile_view, signup_view
from django.contrib.auth import views as auth_views
from django.urls import include, path, reverse_lazy
from core.forms import CustomLoginForm, CustomPasswordChangeForm  # ✅ Include your custom form

app_name = "auth"  # ✅ Namespacing

urlpatterns = [
    # Authentication
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="core/login.html",
            authentication_form=CustomLoginForm  # ✅ Custom login form styling
        ),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path("signup/", signup_view, name="signup"),
    path("profile/", profile_view, name="profile"),
    path("accounts/", include("allauth.urls")),

    # ✅ Password Reset Flow
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="auth/password_reset_form.html",
            email_template_name="auth/password_reset_email.html",
            success_url=reverse_lazy("auth:password_reset_done"),
            extra_email_context={
                "reset_url_name": "auth:password_reset_confirm",
            },
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="auth/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="auth/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="auth/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),

    # ✅ Password Change Flow
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(
            form_class=CustomPasswordChangeForm,  # ✅ Apply custom styling
            template_name="auth/password_change_form.html",
            success_url=reverse_lazy("auth:password_change_done"),
        ),
        name="password_change",
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="auth/password_change_done.html"
        ),
        name="password_change_done",
    ),
]
