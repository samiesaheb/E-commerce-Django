from django.urls import path, include
from core.views import base, about, contact, brands

urlpatterns = [
    path('', base.home, name='home'),
    path('about/', about.about_page, name='about'),
    path('contact/', contact.contact_page, name='contact'),
    path('brands/', brands.brand_index, name='brand-index'),
    path('brands/<slug:slug>/', brands.brand_detail, name='brand-detail'),
    path('products/', include('core.urls.products')),
]
