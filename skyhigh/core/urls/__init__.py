from django.urls import include, path

from core.views import about, base, brands, contact

app_name = "core"

urlpatterns = [
    path("", base.home, name="home"),
    path("about/", about.about_page, name="about"),
    path("contact/", contact.contact_page, name="contact"),
    path("brands/", brands.brand_index, name="brand-index"),
    path("brands/<slug:slug>/", brands.brand_detail, name="brand-detail"),
    path("auth/", include("core.urls.auth", namespace="auth")),
]
