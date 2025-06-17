# core/urls.py

from core.views.checkout import checkout_view
from core.views.contact import contact_page
from core.views.orders import order_detail_view
from core.views.static_pages import privacy_policy_view, terms_and_conditions_view
from core.views.services import services_view, service_detail_view
from django.urls import include, path
from .views import process_payment

app_name = "core"

urlpatterns = [
    path("products/", include("core.urls.products")),
    path("auth/", include("core.urls.auth", namespace="auth")),
    path("cart/", include("core.urls.cart")),
    path("checkout/", checkout_view, name="checkout"),
    path("contact/", contact_page, name="contact"),
    path("process-payment/", process_payment, name="process_payment"),
    path(
        "orders/<int:order_id>/", order_detail_view, name="order_detail"
    ),  # ✅ THIS MUST BE PRESENT
    path("privacy-policy/", privacy_policy_view, name="privacy_policy"),
    path(
        "terms-and-conditions/", terms_and_conditions_view, name="terms_and_conditions"
    ),
    path("services/", services_view, name="services"),
    path("<slug:slug>/", service_detail_view, name="service_detail"),
]
