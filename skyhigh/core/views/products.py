from django.shortcuts import render, get_object_or_404
from core.models import Product

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    # Define slug-to-folder mapping
    image_folder_map = {
        "geometry": "geometry",
        "facial-care": "facialcare",
        "body-and-skin-care": "bodyandskincare",
        "hair-care": "haircare",
    }

    # Get the brand's slug
    brand_slug = product.brand.slug
    image_folder = image_folder_map.get(brand_slug, brand_slug)

    return render(request, "core/product_detail.html", {
        "product": product,
        "image_folder": image_folder,
    })
