from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    slug = models.SlugField(unique=True)
    image = models.CharField(max_length=255, null=True, blank=True)  # e.g., 'geometry/foam.png'
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
