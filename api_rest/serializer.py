from rest_framework import serializers
from .models import Products, Sale, ProductSale

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'price', 'description']

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'total']

class ProductSaleSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source='product.id', read_only=True) 
    nome = serializers.CharField(source='product.name', read_only=True) 
    price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    amount = serializers.IntegerField(source='quantity')

    class Meta:
        model = ProductSale
        fields = ['product_id', 'nome', 'price', 'amount', 'sale']

    def create(self, validated_data):
        quantity = validated_data.pop('quantity')
        sale = validated_data.pop('sale')
        
        product_sale = ProductSale.objects.create(**validated_data, quantity=quantity)
        return product_sale