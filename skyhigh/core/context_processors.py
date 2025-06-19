# core/context_processors.py

from django.conf import settings
from core.models.product import Product  # Adjust if your Product model path differs
from django.templatetags.static import static

def cart_item_count(request):
    cart = request.session.get("cart", {})
    return {
        "cart_item_count": sum(cart.values()),
        "stripe_public_key": settings.STRIPE_PUBLISHABLE_KEY,
        "stripe_secret_key": settings.STRIPE_SECRET_KEY,
    }

def cart_items(request):
    cart = request.session.get("cart", {})
    product_ids = cart.keys()

    products = Product.objects.filter(id__in=product_ids)
    items = []

    for product in products:
        quantity = cart.get(str(product.id), 0)
        items.append({
            "product": product,
            "name": product.name,
            "price": float(product.price),
            "quantity": quantity,
            "image_url": static(f"images/{product.brand}/{product.image}") if isinstance(product.image, str) and product.image else "",
        })

    return {"cart_items": items}
