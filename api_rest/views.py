from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Products, Sale
from .serializer import ProductsSerializer, SaleSerializer

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


@api_view(['POST'])
def create_sale(request):
    serializer = SaleSerializer(data=request.data)
    if serializer.is_valid():
        sale = serializer.save()
        for item in request.data.get('product_sales', []):
            ProductSale.objects.create(
                product_id_id=item['product_id'],
                sale_id=sale,
                price=item['price'],
                quantity=item['quantity']
            )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_sales(request):
    if request.method == 'GET':
        sales = Sale.objects.all()
        serializer = SaleSerializer(sales, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_sale_by_id(request, sale_id):
    try:
        sale = Sale.objects.get(pk=sale_id)
    except Sale.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SaleSerializer(sale)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def cancel_sale(request, sale_id):
    try:
        sale = Sale.objects.get(pk=sale_id)
    except Sale.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        sale.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
def add_products_to_sale(request, sale_id):
    try:
        sale = Sale.objects.get(pk=sale_id)
    except Sale.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        product_ids = request.data.get('product_ids', [])
        products = Products.objects.filter(id__in=product_ids)

        sale.Products.add(*products)

        serializer = SaleSerializer(sale)
        return Response(serializer.data, status=status.HTTP_200_OK)