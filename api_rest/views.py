from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Products, Sale, ProductSale
from .serializers import ProductsSerializer, SaleSerializer, ProductSaleSerializer

@api_view(['GET'])
def get_products(request):
    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def get_product_by_id(request, product_id):
    try:
        product = Products.objects.get(pk=product_id)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductsSerializer(product)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ProductsSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def product_manager(request):
    if request.method == 'GET':
        try:
            if 'id' in request.GET:
                product_id = request.GET['id']
                product = Products.objects.get(pk=product_id)
                serializer = ProductsSerializer(product)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Products.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        new_product = request.data
        serializer = ProductsSerializer(data=new_product)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        product_id = request.data['id']
        try:
            updated_product = Products.objects.get(pk=product_id)
        except Products.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductsSerializer(updated_product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        try:
            product_to_delete = Products.objects.get(pk=request.data['id'])
            product_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except Products.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def sale_manager(request):
    if request.method == 'GET':
        sales = Sale.objects.all()
        serializer = SaleSerializer(sales, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        new_sale = request.data
        serializer = SaleSerializer(data=new_sale)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
