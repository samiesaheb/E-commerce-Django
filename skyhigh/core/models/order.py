# core/models/order.py

from core.models.product import Product
from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    stripe_payment_intent = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Order #{self.id} by {self.full_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
