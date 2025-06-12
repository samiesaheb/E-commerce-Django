from django.db import models
from core.models import Brand

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
