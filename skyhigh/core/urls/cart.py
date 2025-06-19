from core.views import cart
from django.urls import path

app_name = "cart"

urlpatterns = [
    path("add/<int:product_id>/", cart.add_to_cart, name="add"),
    path("show/", cart.view_cart, name="show"),
    path("increment/<int:item_id>/", cart.increment_item, name="increment"),
    path("decrement/<int:item_id>/", cart.decrement_item, name="decrement"),
    path("update/<int:product_id>/", cart.update_quantity, name="update_quantity"),
    path("update-ajax/", cart.update_quantity_ajax, name="update_quantity_ajax"),
    path("remove/<int:product_id>/", cart.remove_from_cart, name="remove"),
]