from django.shortcuts import render, get_object_or_404
from .filters import ProductsFilter
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import product  
from .serializers import productSerializer
from rest_framework.permissions import IsAuthenticated
@api_view(['GET'])
def get_all_products(request):
    products = product.objects.all()  
    serializer = productSerializer(products, many=True)
    print(products)
    return Response({"products": serializer.data})  

@api_view(['GET'])
def get_specified_product(request,pk):
    products=get_object_or_404(request,id=pk)
    serializer=productSerializer(products, many=False)
    return Response({"products": serializer.data})  
    
  
@api_view(['GET'])
def filter_products(request):
    filterset=ProductsFilter(request.GET,queryset=product.object.all().order_by('id'))
    serializer = productSerializer(filterset, many=True)
    return Response({"products": serializer.data})  

@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def new_products(request):
    data=request.data
    serializer=productSerializer(data=data)
    if serializer.is_valid():
        Product=product.Object.create(**data,user=request.user)
        res=productSerializer(Product,many=False)  
        return Response({"product":res.data})
    else:
        return Response(serializer.errors)
    
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated]) 
def edit_products(request,pk):
    product=get_specified_product(request,id=pk)
    if product.user!=request.user:
        return Response({"message":"you can't edit this product"})
    data=request.data
    serializer=productSerializer(instance=product,data=data)
    if serializer.is_valid():
        Product=product.Object.create(**data,user=request.user)
        res=productSerializer(Product,many=False)  
        return Response({"product":res.data})
    else:
        return Response(serializer.errors)
    
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated]) 
def delete_products(request,pk):
    product=get_specified_product(request,id=pk)
    if product.user!=request.user:
        return Response({"message":"you can't edit this product"})
    product.delete()
    return Response({"message":"product deleted"})