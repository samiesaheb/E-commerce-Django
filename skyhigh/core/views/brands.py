from django.shortcuts import get_object_or_404, render

from core.models import Brand, Product


def brand_index(request):
    brands = Brand.objects.all()
    return render(request, "brands/index.html", {"brands": brands})


def brand_detail(request, slug):
    # Get brand or return 404 if not found
    brand = get_object_or_404(Brand, slug=slug)

    # Get all products associated with this brand
    products = Product.objects.filter(brand=brand)

    # Define a map from brand slugs to their respective static image folder names
    image_folder_map = {
        "geometry": "geometry",
        "facial-care": "facialcare",
        "body-and-skin-care": "bodyandskincare",
        "hair-care": "haircare",
    }

    # Resolve the correct folder or use brand.slug as fallback
    image_folder = image_folder_map.get(slug, slug)

    return render(
        request,
        "core/brand_detail.html",
        {
            "brand": brand,
            "products": products,
            "image_folder": image_folder,
        },
    )
