from django.contrib import admin
from core.models.brand import Brand
from core.models.product import Product
from django.contrib.auth.models import User

admin.site.register(Brand)
admin.site.register(Product)

admin.site.unregister(User)
# Register a custom UserAdmin if needed
