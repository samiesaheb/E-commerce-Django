# core/views/auth.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from core.forms import SignUpForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from core.models.order import Order

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'  # 👈 Important for multiple backends
            login(request, user)
            return redirect('auth:profile')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})

@login_required
def profile_view(request):
    editing = request.GET.get("edit") == "true"
    success = False

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            if form.has_changed():  # ✅ Only save and redirect if something actually changed
                form.save()
                return redirect('/auth/profile/?edit=false&updated=1')
            else:
                return redirect('/auth/profile/?edit=false&updated=0')  # No change
    else:
        form = UserUpdateForm(instance=request.user)

    # ✅ Fetch orders for the logged-in user
    orders = Order.objects.filter(user=request.user).order_by("-created_at")

    return render(request, 'core/profile.html', {
        'form': form,
        'editing': editing,
        'success': request.GET.get("updated") == "1",
        'orders': orders
    })
