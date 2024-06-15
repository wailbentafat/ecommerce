from django.shortcuts import render, get_object_or_404
from .filters import ProductsFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import product  
from .serializers import productSerializer

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
  
