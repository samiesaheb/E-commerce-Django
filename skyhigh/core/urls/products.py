from django.urls import path
from core.views.products import product_detail  # Adjust if view is elsewhere

urlpatterns = [
    path('<slug:slug>/', product_detail, name='product-detail'),
]
