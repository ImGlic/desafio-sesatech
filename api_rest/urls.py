from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.get_products),
    path('products', views.get_products, name='get_all_products'),
    path('product/<int:product_id>/', views.get_product_by_id, name='get_product_by_id'), 
    path('product_manager/', views.product_manager, name='product_manager'), 

    path('sales/', views.create_sale, name='create_sale'),
    path('sales/list/', views.list_sales, name='list_sales'),
    path('sales/list/<int:sale_id>/', views.get_sale_by_id, name='get_sale_by_id'),
    path('sales/<int:sale_id>/cancel/', views.cancel_sale, name='cancel_sale'),
    path('sales/<int:sale_id>/add_products/', views.add_products_to_sale, name='add_products_to_sale'),
]
