from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from core.models.product import Product
from core.models.brand import Brand
from core.models.order import Order

@staff_member_required
def dashboard_home(request):
    context = {
        "total_products": Product.objects.count(),
        "total_brands": Brand.objects.count(),
        "total_orders": Order.objects.count(),
        "total_revenue": sum(order.total_price() for order in Order.objects.all()),
    }
    return render(request, 'admin/dashboard_home.html', context)

@staff_member_required
def manage_products(request):
    products = Product.objects.all()
    return render(request, 'admin/manage_products.html', {'products': products})

@staff_member_required
def manage_brands(request):
    brands = Brand.objects.all()
    return render(request, 'admin/manage_brands.html', {'brands': brands})

@staff_member_required
def manage_orders(request):
    orders = Order.objects.all()
    return render(request, 'admin/manage_orders.html', {'orders': orders})
