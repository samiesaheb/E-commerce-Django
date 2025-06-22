import os
import sys
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skyhigh.settings')
sys.path.append(os.path.dirname(os.path.dirname(__file__)))  # Adds project root to path

django.setup()

from core.models import Product

STATIC_DIR = os.path.join(os.path.dirname(__file__), '../core/static/images')

for product in Product.objects.all():
    if not product.main_image:
        brand_slug = product.brand.name.lower().replace(" ", "")
        image_path = os.path.join(STATIC_DIR, brand_slug, f"{product.slug}.jpg")

        if os.path.exists(image_path):
            with open(image_path, 'rb') as img_file:
                product.main_image.save(f"{product.slug}.jpg", File(img_file), save=True)
                print(f"✅ Assigned image to: {product.name}")
        else:
            print(f"⚠️ No image found for: {product.name}")
