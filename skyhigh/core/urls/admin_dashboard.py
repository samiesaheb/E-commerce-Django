from django.urls import path
from core.views import admin_dashboard

urlpatterns = [
    path('', admin_dashboard.dashboard_home, name='admin_dashboard_home'),
    path('products/', admin_dashboard.manage_products, name='admin_manage_products'),
    path('brands/', admin_dashboard.manage_brands, name='admin_manage_brands'),
    path('orders/', admin_dashboard.manage_orders, name='admin_manage_orders'),
]
