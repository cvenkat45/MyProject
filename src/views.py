from django.shortcuts import render
from .models import Products
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
# from django.http import HttpResponse


def srcindex(request):
    return render(request, 'srcindex.html')


@api_view(['GET'])
def products_api(request):
    products = Products.objects.all().order_by('id')
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def products_details_api(request, pk):
    product = get_object_or_404(Products, id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_product_api(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def edit_product_api(request, pk):
    product = get_object_or_404(Products, id=pk)
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    print(request.data)
    return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)


@api_view(['DELETE'])
def delete_product_api(request, pk):
    if request.is_ajax():
        product = get_object_or_404(Products, id=pk)
        product.delete()
        return Response('Product successfully Deleted!', status=status.HTTP_200_OK)

    return Response("That Product Doesn't Exist!", status=status.HTTP_204_NO_CONTENT)
