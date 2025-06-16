# core/views/checkout.py

from django.shortcuts import render, redirect
from core.models import Product, CartItem, Order, OrderItem
from typing import Dict, List
from django.db.models import QuerySet
from typing import cast
import stripe
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY

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
        cart_items.append({
            "product": product,
            "quantity": quantity,
            "id": product.id
        })

    return render(request, "core/checkout.html", {
        "cart_items": cart_items,
        "total": total
    })

def process_payment(request):
    if request.method == "POST":
        payment_method_id = request.POST.get("payment_method_id")
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        city = request.POST.get("city")
        postal_code = request.POST.get("postal_code")
        country = request.POST.get("country")

        cart = request.session.get("cart", {})
        if not cart:
            return render(request, "core/payment_failed.html", {"error": "Your cart is empty."})

        try:
            # Calculate total
            products = Product.objects.filter(id__in=cart.keys())
            total = sum(product.price * cart[str(product.id)] for product in products)

            # Create Stripe PaymentIntent
            intent = stripe.PaymentIntent.create(
                amount=int(total * 100),  # amount in paisa
                currency="inr",
                payment_method=payment_method_id,
                confirm=True,
                automatic_payment_methods={
                    "enabled": True,
                    "allow_redirects": "never"
                }
            )

            # ✅ Save order
            order = Order.objects.create(
                user=request.user if request.user.is_authenticated else None,
                full_name=full_name,
                email=email,
                address=address,
                city=city,
                postal_code=postal_code,
                country=country,
                total_price=total,
                stripe_payment_intent=intent.id
            )

            for product in products:
                quantity = cart[str(product.id)]
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    price=product.price
                )

            # ✅ Clear the cart
            request.session["cart"] = {}

            # ✅ Send confirmation email BEFORE returning
            send_mail(
                subject="Order Confirmation - Sky High",
                message=(
                    f"Dear {order.full_name},\n\n"
                    f"Thank you for your purchase at Sky High International!\n\n"
                    f"Order ID: #{order.id}\n"
                    f"Total: ₹{order.total_price}\n\n"
                    f"We're processing your order and will notify you once it's shipped.\n\n"
                    f"Shipping Address:\n{order.address}, {order.city}, {order.postal_code}, {order.country}\n\n"
                    f"Warm regards,\nSky High Team"
                ),
                from_email="no-reply@skyhigh.com",
                recipient_list=[order.email],
                fail_silently=False,
            )

            return render(request, "core/payment_success.html", {"order": order})

        except stripe.error.CardError as e:
            return render(request, "core/payment_failed.html", {"error": str(e)})
        except Exception as e:
            return render(request, "core/payment_failed.html", {"error": str(e)})

    return redirect("checkout")
