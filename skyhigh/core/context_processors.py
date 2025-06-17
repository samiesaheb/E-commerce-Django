from django.conf import settings


def cart_item_count(request):
    cart = request.session.get("cart", {})
    return {
        "cart_item_count": sum(cart.values()),
        "stripe_public_key": settings.STRIPE_PUBLISHABLE_KEY,
        "stripe_secret_key": settings.STRIPE_SECRET_KEY,  # Only if absolutely needed
    }
