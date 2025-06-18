from core.views.services import services_view, service_detail_view
from django.urls import path

app_name = "services"

urlpatterns = [
    path("", services_view, name="index"),  # ✅ now this works with {% url 'services:index' %}
    path("<slug:slug>/", service_detail_view, name="service_detail"),
]
