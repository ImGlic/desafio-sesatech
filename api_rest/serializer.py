from rest_framework import serializers
from .models import Products, Sale

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'price', 'description']

class SaleSerializer(serializers.ModelSerializer):
    products = ProductsSerializer(many=True, read_only=True)  
    product_ids = serializers.ListField(
        child=serializers.IntegerField(), write_only=True  
    )

    class Meta:
        model = Sale
        fields = ['id', 'total', 'products', 'product_ids']

    def create(self, validated_data):
        product_ids = validated_data.pop('product_ids', [])
        
        sale = Sale.objects.create(**validated_data)

        products = Products.objects.filter(id__in=product_ids)
        sale.products.set(products)
        return sale
