from django.urls import path

from core.views import cart

app_name = "cart"

urlpatterns = [
    path("add/<int:product_id>/", cart.add_to_cart, name="add"),
    path("show/", cart.view_cart, name="show"),
    path("increment/<int:item_id>/", cart.increment_item, name="increment"),
    path("decrement/<int:item_id>/", cart.decrement_item, name="decrement"),
]
