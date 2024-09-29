from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('products', views.get_products, name='get_all_products'),

    path('product/<int:product_id>/', views.get_product_by_id, name='get_product_by_id'), 
    path('product_manager/', views.product_manager, name='product_manager'), 

    path('sales/', views.sale_manager, name='sale_manager'), 
]
