from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from core.models.product import Product
from core.models.brand import Brand
from core.models.order import Order
from core.forms import AdminProductForm, AdminBrandForm
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
import csv
from core.models.product import ProductAnalytics
from django.db.models import Sum
from datetime import timedelta, date
from django.contrib.auth.models import User
from core.models.user_analytics import UserAnalytics


@staff_member_required
def dashboard_home(request):
    today = date.today()

    total_products = Product.objects.count()
    total_brands = Brand.objects.count()
    total_orders = Order.objects.count()
    total_revenue = sum(order.total_price for order in Order.objects.all())

    new_users_today = UserAnalytics.objects.filter(event_type="signup", timestamp__date=today).count()
    logins_today = UserAnalytics.objects.filter(event_type="login", timestamp__date=today).count()

    context = {
        "total_products": total_products,
        "total_brands": total_brands,
        "total_orders": total_orders,
        "total_revenue": total_revenue,
        "new_users_today": new_users_today,
        "logins_today": logins_today,
    }

    return render(request, 'admin/dashboard_home.html', context)


from django.core.paginator import Paginator
from django.db.models import Q

@staff_member_required
def manage_products(request):
    query = request.GET.get("q", "")
    product_list = Product.objects.all().select_related("brand")

    if query:
        product_list = product_list.filter(
            Q(name__icontains=query) |
            Q(slug__icontains=query) |
            Q(brand__name__icontains=query)
        )

    paginator = Paginator(product_list, 10)  # Show 10 products per page
    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)

    return render(request, "admin/manage_products.html", {
        "products": products,
        "query": query,
    })


@staff_member_required
def manage_brands(request):
    query = request.GET.get("q", "")
    brands = Brand.objects.all()

    if query:
        brands = brands.filter(
            models.Q(name__icontains=query) | models.Q(slug__icontains=query)
        )

    paginator = Paginator(brands, 10)
    page = request.GET.get("page")
    paginated = paginator.get_page(page)

    return render(request, 'admin/manage_brands.html', {
        'brands': paginated,
        'query': query
    })

@staff_member_required
def manage_orders(request):
    query = request.GET.get("q", "")
    orders_qs = Order.objects.select_related("user").order_by("-created_at")

    if query:
        orders_qs = orders_qs.filter(
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query) |
            Q(user__username__icontains=query) |
            Q(email__icontains=query)
        )

    paginator = Paginator(orders_qs, 10)  # Show 10 orders per page
    page_number = request.GET.get("page")
    orders = paginator.get_page(page_number)

    return render(request, 'admin/manage_orders.html', {
        'orders': orders,
        'query': query,
    })


@staff_member_required
def create_product(request):
    if request.method == "POST":
        form = AdminProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f"✅ Product '{product.name}' created successfully.")
            return redirect("admin_manage_products")
        else:
            messages.error(request, "❌ There was an error creating the product. Please check the form.")
    else:
        form = AdminProductForm()

    return render(request, "admin/create_product.html", {"form": form})

@staff_member_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = AdminProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f"✅ Product '{product.name}' updated successfully.")
            return redirect("admin_manage_products")
        else:
            messages.error(request, "❌ There was an error updating the product.")
    else:
        form = AdminProductForm(instance=product)

    return render(request, "admin/edit_product.html", {"form": form, "product": product})

@staff_member_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.success(request, f"🗑️ Product '{product.name}' deleted successfully.")
    return redirect("admin_manage_products")


@staff_member_required
def create_brand(request):
    if request.method == "POST":
        form = AdminBrandForm(request.POST)
        if form.is_valid():
            brand = form.save()
            messages.success(request, f"✅ Brand '{brand.name}' created successfully.")
            return redirect("admin_manage_brands")
        else:
            messages.error(request, "❌ There was an error creating the brand.")
    else:
        form = AdminBrandForm()
    return render(request, "admin/create_brand.html", {"form": form})

@staff_member_required
def edit_brand(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    if request.method == "POST":
        form = AdminBrandForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            messages.success(request, f"✅ Brand '{brand.name}' updated successfully.")
            return redirect("admin_manage_brands")
        else:
            messages.error(request, "❌ There was an error updating the brand.")
    else:
        form = AdminBrandForm(instance=brand)
    return render(request, "admin/edit_brand.html", {"form": form, "brand": brand})

@staff_member_required
def delete_brand(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    brand.delete()
    messages.success(request, f"🗑️ Brand '{brand.name}' deleted successfully.")
    return redirect("admin_manage_brands")


@staff_member_required
def fulfill_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.is_fulfilled = True
    order.save()
    messages.success(request, f"✅ Order #{order_id} marked as fulfilled.")
    return redirect("admin_manage_orders")


from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
import tempfile

@staff_member_required
def download_invoice(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    logo_url = request.build_absolute_uri('/static/images/logo.jpg')
    html_string = render_to_string("admin/invoice_template.html", {
        "order": order,
        "logo_url": logo_url,
    })

    with tempfile.NamedTemporaryFile(delete=True) as tmp_file:
        HTML(string=html_string, base_url=request.build_absolute_uri()).write_pdf(tmp_file.name)
        tmp_file.seek(0)
        response = HttpResponse(tmp_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'filename=invoice_order_{order.id}.pdf'
        return response

from django.http import JsonResponse
from django.db.models import Q
from django.urls import reverse

@staff_member_required
def search_products(request):
    q = request.GET.get("q", "")
    products = Product.objects.filter(
        Q(name__icontains=q) | Q(slug__icontains=q) | Q(brand__name__icontains=q)
    ).select_related("brand")[:20]

    results = [{
        "id": p.id,
        "name": p.name,
        "slug": p.slug,
        "price": str(p.price),
        "brand": p.brand.name,
        "image": p.static_image_url,
        "edit_url": reverse("admin_edit_product", args=[p.id]),
        "delete_url": reverse("admin_delete_product", args=[p.id]),
    } for p in products]

    return JsonResponse({"results": results})


@staff_member_required
def search_brands(request):
    q = request.GET.get("q", "")
    brands = Brand.objects.filter(
        Q(name__icontains=q) | Q(slug__icontains=q)
    )[:20]

    results = [{
        "id": b.id,
        "name": b.name,
        "description": b.description,
        "edit_url": reverse("admin_edit_brand", args=[b.id]),
        "delete_url": reverse("admin_delete_brand", args=[b.id]),
    } for b in brands]

    return JsonResponse({"results": results})


@staff_member_required
def search_orders(request):
    q = request.GET.get("q", "")
    orders = Order.objects.filter(
        Q(full_name__icontains=q) |
        Q(email__icontains=q) |
        Q(id__icontains=q)
    ).select_related("user")[:20]

    results = [{
        "id": o.id,
        "customer": o.user.get_full_name() if o.user else o.full_name,
        "total_price": str(o.total_price),
        "status": "Fulfilled" if o.is_fulfilled else "Pending",
        "created": o.created_at.strftime("%Y-%m-%d %H:%M"),
        "detail_url": reverse("admin_order_detail", args=[o.id]),
    } for o in orders]

    return JsonResponse({"results": results})


@staff_member_required
@require_POST
def bulk_delete_products(request):
    ids = request.POST.getlist('selected_ids')
    Product.objects.filter(id__in=ids).delete()
    messages.success(request, f"{len(ids)} product(s) deleted successfully.")
    return redirect('admin_manage_products')

@staff_member_required
def export_products_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'Slug', 'Brand', 'Price'])

    for product in Product.objects.select_related('brand').all():
        writer.writerow([product.id, product.name, product.slug, product.brand.name, product.price])

    return response

from core.models.product import Product, ProductAnalytics
from datetime import timedelta, date
from django.utils.dateparse import parse_date

def product_analytics_dashboard(request):
    # Handle filters
    product_id = request.GET.get("product_id")
    start_date = parse_date(request.GET.get("start_date") or "") or date.today() - timedelta(days=30)
    end_date = parse_date(request.GET.get("end_date") or "") or date.today()

    # Base queryset
    queryset = ProductAnalytics.objects.filter(date__range=(start_date, end_date))

    if product_id and product_id.isdigit():
        queryset = queryset.filter(product_id=product_id)

    aggregated = (
        queryset
        .values("product_id", "date")
        .annotate(total_views=Sum("view_count"), total_cart_adds=Sum("cart_add_count"))
        .order_by("date")
    )

    product_map = {p.id: p.name for p in Product.objects.all()}
    data = [
        {
            "product_name": product_map.get(row["product_id"], "Unknown"),
            "date": row["date"].isoformat(),
            "total_views": row["total_views"],
            "total_cart_adds": row["total_cart_adds"],
        }
        for row in aggregated
    ]

    return render(request, "admin/product_analytics.html", {
        "analytics_data": data,
        "products": Product.objects.all(),
        "selected_product_id": int(product_id) if product_id and product_id.isdigit() else None,
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
    })


def export_product_analytics_csv(request):
    product_id = request.GET.get("product_id")
    start_date = parse_date(request.GET.get("start_date") or "")
    end_date = parse_date(request.GET.get("end_date") or "")

    queryset = ProductAnalytics.objects.all()

    if start_date and end_date:
        queryset = queryset.filter(date__range=(start_date, end_date))
    if product_id and product_id.isdigit():
        queryset = queryset.filter(product_id=product_id)

    # Prepare CSV
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="product_analytics.csv"'

    writer = csv.writer(response)
    writer.writerow(["Product", "Date", "Views", "Cart Adds"])

    for entry in queryset.select_related("product").order_by("date"):
        writer.writerow([
            entry.product.name,
            entry.date.isoformat(),
            entry.view_count,
            entry.cart_add_count,
        ])

    return response
