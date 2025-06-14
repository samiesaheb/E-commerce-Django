# core/urls.py
from django.urls import include, path

from core.views.checkout import checkout_view  # ✅ import your new view
from core.views.contact import contact_page

urlpatterns = [
    # other includes like brands, etc.
    path("products/", include("core.urls.products")),
    path("auth/", include("core.urls.auth", namespace="auth")),
    path("cart/", include("core.urls.cart")),
    path("checkout/", checkout_view, name="checkout"),  # ✅ define the route with name
    path("contact/", contact_page, name="contact"),
]
