from typing import Dict, List, cast

from core.models import Product
from django.db.models import QuerySet
from django.http import JsonResponse, HttpRequest, HttpResponse,  HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
import json


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
    cart_count = sum(cart.values())

    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return JsonResponse({"success": True, "cart_count": cart_count})

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
        cart_items.append({"product": product, "quantity": quantity, "id": product.id})

    return render(request, "core/cart.html", {"cart_page_items": cart_items, "total": total})


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


# ✅ NEW: Update quantity to a specific value
@require_POST
def update_quantity(request: HttpRequest, product_id: int) -> HttpResponse:
    try:
        new_quantity = int(request.POST.get("quantity", 1))
        if new_quantity < 1:
            return remove_from_cart(request, product_id)
    except (TypeError, ValueError):
        return redirect("cart:show")

    cart = request.session.get("cart", {})
    cart[str(product_id)] = new_quantity
    request.session["cart"] = cart
    return redirect("cart:show")

# AJAX endpoint to update quantity and return JSON
@require_POST
def update_quantity_ajax(request: HttpRequest) -> JsonResponse:
    try:
        payload = json.loads(request.body.decode())
        product_id = int(payload.get("product_id"))
        quantity = int(payload.get("quantity", 1))
    except (TypeError, ValueError, json.JSONDecodeError):
        return JsonResponse({"success": False}, status=400)

    cart = request.session.get("cart", {})
    if quantity < 1:
        cart.pop(str(product_id), None)
    else:
        cart[str(product_id)] = quantity
    request.session["cart"] = cart
    cart_count = sum(cart.values())
    return JsonResponse({"success": True, "count": cart_count})



# ✅ NEW: Remove an item from the cart
def remove_from_cart(request, product_id):
    if request.method == 'POST':
        # ... your existing logic to remove item ...
        cart = request.session.get('cart', {})
        cart.pop(str(product_id), None)
        request.session['cart'] = cart

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({ 'success': True, 'count': sum(item['quantity'] for item in cart.values()) })
        else:
            return HttpResponseRedirect('/cart/show/')  # fallback for regular POST

    return JsonResponse({ 'error': 'Invalid request method' }, status=400)
