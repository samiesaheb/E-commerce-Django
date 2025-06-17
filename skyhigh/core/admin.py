from core.models.brand import Brand
from core.models.order import Order  # Add this if managing orders
from core.models.product import Product
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "price", "slug")
    list_filter = ("brand",)
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created_at", "total_price")
    list_filter = ("created_at",)
    search_fields = ("user__username",)


# Optional: Re-register User with customization
admin.site.unregister(User)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
