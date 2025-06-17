from django.urls import path
from core.views.products import (
    product_detail,
    product_list,
    product_search,
    product_autocomplete,
)

app_name = "products"

urlpatterns = [
    path("search/", product_search, name="search"),
    path("autocomplete/", product_autocomplete, name="autocomplete"),  # ✅ Match 'autocomplete'
    path("", product_list, name="list"),
    path("<slug:slug>/", product_detail, name="product-detail"),
]
