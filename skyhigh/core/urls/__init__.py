from django.urls import path, include
from core.views import base, about, contact, brands
from core.views.orders import order_detail_view
from core.views.static_pages import privacy_policy_view, terms_and_conditions_view
app_name = "core"

urlpatterns = [
    path('', base.home, name='home'),
    path('about/', about.about_page, name='about'),
    path('contact/', contact.contact_page, name='contact'),
    path('brands/', brands.brand_index, name='brand-index'),
    path('brands/<slug:slug>/', brands.brand_detail, name='brand-detail'),
    path("auth/", include("core.urls.auth", namespace="auth")),
    # Order detail page for users to view a single order
    path('orders/<int:order_id>/', order_detail_view, name='order_detail'),
    path("privacy-policy/", privacy_policy_view, name="privacy_policy"),
    path("terms-and-conditions/", terms_and_conditions_view, name="terms_and_conditions"),
]
