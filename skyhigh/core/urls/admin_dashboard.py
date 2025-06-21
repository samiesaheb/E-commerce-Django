from django.urls import path
from core.views import admin_dashboard

urlpatterns = [
    path('', admin_dashboard.dashboard_home, name='admin_dashboard_home'),
    path('products/', admin_dashboard.manage_products, name='admin_manage_products'),
    path('products/create/', admin_dashboard.create_product, name='admin_create_product'),
    path('products/edit/<int:pk>/', admin_dashboard.edit_product, name='admin_edit_product'),
    path('products/delete/<int:pk>/', admin_dashboard.delete_product, name='admin_delete_product'),
    path('products/search/', admin_dashboard.search_products, name='admin_search_products'),
    path('products/bulk-delete/', admin_dashboard.bulk_delete_products, name='admin_bulk_delete_products'),
    path('products/export-csv/', admin_dashboard.export_products_csv, name='admin_export_products_csv'),  # ✅ Add this line

    path('brands/', admin_dashboard.manage_brands, name='admin_manage_brands'),
    path('brands/create/', admin_dashboard.create_brand, name='admin_create_brand'),
    path('brands/edit/<int:pk>/', admin_dashboard.edit_brand, name='admin_edit_brand'),
    path('brands/delete/<int:pk>/', admin_dashboard.delete_brand, name='admin_delete_brand'),

    path('orders/', admin_dashboard.manage_orders, name='admin_manage_orders'),
    path('orders/fulfill/<int:order_id>/', admin_dashboard.fulfill_order, name='admin_fulfill_order'),
    path('orders/invoice/<int:order_id>/', admin_dashboard.download_invoice, name='admin_download_invoice'),
]
