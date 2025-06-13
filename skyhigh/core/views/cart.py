from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_POST
from core.models import Product
from typing import Dict, List
from django.db.models import QuerySet
from typing import cast

@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get("cart", {})
    product_id_str = str(product.id)

    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1

    request.session["cart"] = cart

    # Redirect back to the same page
    return redirect(request.META.get("HTTP_REFERER", "/"))


def view_cart(request):
    cart: Dict[str, int] = request.session.get("cart", {})
    product_ids: List[int] = [int(pid) for pid in cart.keys()]

    products: QuerySet[Product] = Product.objects.filter(id__in=product_ids)

    cart_items = []
    total = 0

    for product in products:
        product = cast(Product, product)
        product_id_str = str(product.id)
        quantity = cart.get(product_id_str, 0)
        if product.price:
            total += product.price * quantity
        cart_items.append({
            "product": product,
            "quantity": quantity,
            "id": product.id
        })

    return render(request, "core/cart.html", {"cart_items": cart_items, "total": total})


def increment_item(request, item_id):
    cart = request.session.get("cart", {})
    item_id = str(item_id)
    if item_id in cart:
        cart[item_id] += 1
        request.session["cart"] = cart
    return redirect("cart:show")

def decrement_item(request, item_id):
    cart = request.session.get("cart", {})
    item_id = str(item_id)
    if item_id in cart:
        if cart[item_id] > 1:
            cart[item_id] -= 1
        else:
            del cart[item_id]
        request.session["cart"] = cart
    return redirect("cart:show")
