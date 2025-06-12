# core/urls.py
from django.urls import path, include

urlpatterns = [
    # other includes like brands, etc.
    path('products/', include('core.urls.products')),
]
