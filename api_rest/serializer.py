from rest_framework import serializers
from .models import Products, Sale, ProductSale

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'price', 'description']

class ProductSaleSerializer(serializers.ModelSerializer):
    product = ProductsSerializer()

    class Meta:
        model = ProductSale
        fields = ['product', 'quantity', 'sale_price']

class SaleSerializer(serializers.ModelSerializer):
    product_sales = ProductSaleSerializer(source='productsale_set', many=True)

    class Meta:
        model = Sale
        fields = ['id', 'sale_date', 'product_sales', 'total_value']
