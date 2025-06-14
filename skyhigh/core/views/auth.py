# core/views/auth.py

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from core.forms import SignUpForm


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = "django.contrib.auth.backends.ModelBackend"
            # 👈 Important for multiple backends
            login(request, user)
            return redirect("auth:profile")
    else:
        form = SignUpForm()
    return render(request, "core/signup.html", {"form": form})


@login_required
def profile_view(request):
    user = request.user

    # Use this for debugging: pass user attributes explicitly
    user_info = {
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
    }

    return render(
        request,
        "core/profile.html",
        {
            "user": user,
            "user_info": user_info,
        },
    )
