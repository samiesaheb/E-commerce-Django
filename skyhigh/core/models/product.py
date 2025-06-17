from core.models import Brand
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    brand = models.ForeignKey(Brand, related_name="products", on_delete=models.CASCADE)

    @property
    def image(self) -> str:
        """Return the expected image filename for this product."""
        return f"{self.slug}.jpg"

    def __str__(self):
        return self.name
