from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view 
from rest_framework.response import Response

from .models import Product
# from .products import products
from .serializers import ProductSerializer

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        
    ]
    return Response(routes)

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many = True)
    return Response(serializer.data)

# @api_view(['GET'])
# def getProducts(requests):
#     return Response(products)

# @api_view(['GET'])
# def getProduct(requests, pk):
#     product = None
#     for i in products:
#         if i['_id'] == pk:
#             product = i
#             break
#     return Response(product)


@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
