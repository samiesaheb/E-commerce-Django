from core.models import Product
from django.db.models import Q  # For search functionality
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.templatetags.static import static



# Detail View: Shows a single product
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    # Map known brand slugs to their image folders
    image_folder_map = {
        "geometry": "geometry",
        "facial-care": "facialcare",
        "body-and-skin-care": "bodyandskincare",
        "hair-care": "haircare",
    }

    image_folder = image_folder_map.get(product.brand.slug, "default")

    context = {
        "product": product,
        "image_folder": image_folder,
    }
    return render(request, "core/product_detail.html", context)


# List View: Shows all products (optional if you're only listing by brand)
def product_list(request):
    products = (
        Product.objects.all().select_related("brand").order_by("brand__name", "name")
    )

    context = {
        "products": products,
    }
    return render(request, "core/product_list.html", context)


# Search View: Returns products matching query
def product_search(request):
    query = request.GET.get("q", "")
    results = []

    if query:
        results = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        ).select_related("brand")

    context = {"query": query, "results": results}
    return render(request, "core/product_search.html", context)

def product_autocomplete(request):
    query = request.GET.get("q", "")
    if query:
        products = Product.objects.filter(name__icontains=query)[:30]
        results = []
        for p in products:
            # Derive folder from brand slug (matches your static subfolder structure)
            folder = p.brand.slug.replace('-', '')
            image_path = f"images/{folder}/{p.image}" if p.image else "images/placeholder.jpg"

            results.append({
                "name": p.name,
                "slug": p.slug,
                "image_url": static(image_path),
            })
    else:
        results = []

    return JsonResponse({"results": results})
