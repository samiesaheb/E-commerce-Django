# core/forms.py

from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm,
)
from django.contrib.auth.models import User
from core.models import Product

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update(
                {"class": "w-full border border-gray-300 rounded p-2"}
            )


class CustomLoginForm(AuthenticationForm):
    """Login form with Tailwind CSS styling."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update(
                {"class": "w-full border border-gray-300 rounded p-2"}
            )


class CustomPasswordChangeForm(PasswordChangeForm):
    """Password change form with Tailwind CSS styling."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update(
                {"class": "w-full border border-gray-300 rounded p-2"}
            )

class AdminProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "brand", "price", "description", "slug", "main_image"]  # ← Added main_image
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4, "class": "w-full border rounded p-2"}),
            "name": forms.TextInput(attrs={"class": "w-full border rounded p-2"}),
            "slug": forms.TextInput(attrs={"class": "w-full border rounded p-2"}),
            "price": forms.NumberInput(attrs={"class": "w-full border rounded p-2"}),
            "brand": forms.Select(attrs={"class": "w-full border rounded p-2"}),
            "main_image": forms.ClearableFileInput(attrs={"class": "w-full border rounded p-2"}),  # ← Add this
        }

from core.models import Brand

class AdminBrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'slug']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full border rounded p-2'}),
            'slug': forms.TextInput(attrs={'class': 'w-full border rounded p-2'}),
        }
