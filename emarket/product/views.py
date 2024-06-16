from django.shortcuts import render, get_object_or_404
from .filters import ProductsFilter
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response 
from .models import product  
from .serializers import productSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
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
    try:
      data=request.data
      print({"data":data})
      
      serializer=productSerializer(data=data)
      print({"serializer":serializer})
      if serializer.is_valid():
            # Save the validated data and associate it with the current user
            product_instance = serializer.save(user=request.user)
            serialized_product = productSerializer(product_instance, many=False)
            return Response({"product": serialized_product.data}, status=status.HTTP_201_CREATED)
      else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    except Exception as e:
        print(e)
        return Response({"message": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated]) 
def edit_products(request,pk):
    try:
        product_instance = get_object_or_404(product, id=pk)
    except product.DoesNotExist:
        return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    if product_instance.user != request.user:
        return Response({"message": "You are not authorized to edit this product"}, status=status.HTTP_403_FORBIDDEN)

    data = request.data
    serializer = productSerializer(instance=product_instance, data=data)
    if serializer.is_valid():
        serializer.save()  # Save the updated product instance
        return Response({"product": serializer.data})
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

@api_view(['PUT'])
@permission_classes([IsAuthenticated]) 
def delete_products(request,pk):
    product=get_specified_product(request,id=pk)
    if product.user!=request.user:
        return Response({"message":"you can't edit this product"})
    product.delete()
    return Response({"message":"product deleted"})