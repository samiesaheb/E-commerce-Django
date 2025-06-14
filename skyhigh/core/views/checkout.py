from typing import Dict, List, cast

from django.db.models import QuerySet
from django.shortcuts import render

from core.models import Product


def checkout_view(request):
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

    return render(
        request, "core/checkout.html", {"cart_items": cart_items, "total": total}
    )
