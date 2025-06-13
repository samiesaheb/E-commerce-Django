# core/urls/products.py
from django.urls import path
from core.views.products import product_detail, product_list, product_search

app_name = "products"  # Important for {% url 'products:...' %} to work

urlpatterns = [
    path("search/", product_search, name="search"),
    path("", product_list, name="list"),
    path("<slug:slug>/", product_detail, name="product-detail"),
]
