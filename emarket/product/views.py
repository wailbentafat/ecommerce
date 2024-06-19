# views.py
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db.models import Avg
from .models import product  
from .serializers import productSerializer

@api_view(['GET'])
def get_all_products(request):
    products = product.objects.all()  
    serializer = productSerializer(products, many=True)
    return Response({"products": serializer.data})  

@api_view(['GET'])
def get_specified_product(request, pk):
    product_instance = get_object_or_404(product, id=pk)
    serializer = productSerializer(product_instance, many=False)
    return Response({"product": serializer.data})  
    
@api_view(['GET'])
def filter_products(request):
    filterset = ProductsFilter(request.GET, queryset=product.objects.all().order_by('id'))
    serializer = productSerializer(filterset.qs, many=True)
    return Response({"products": serializer.data})  

@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def new_products(request):
    try:
        data = request.data
        serializer = productSerializer(data=data)
        if serializer.is_valid():
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
def edit_products(request, pk):
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

@api_view(['DELETE'])
@permission_classes([IsAuthenticated]) 
def delete_products(request, pk):
    product_instance = get_object_or_404(product, id=pk)
    if product_instance.user != request.user:
        return Response({"message": "You are not authorized to delete this product"}, status=status.HTTP_403_FORBIDDEN)

    product_instance.delete()
    return Response({"message": "Product deleted"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def add_review(request, pk):
    user = request.user
    product_instance = get_object_or_404(product, id=pk)
    data = request.data
    review = product_instance.reviews.filter(user=user)
    
    if int(data['rating']) <= 0 or int(data['rating']) > 10:
        return Response({"error": "Select a rating between 1 and 10"}, status=status.HTTP_400_BAD_REQUEST)
    
    if review.exists():
        new_review = {"rating": data['rating'], 'comment': data['comment']}
        review.update(**new_review)
    else:
        review.objects.create(
            user=user,
            product=product_instance,
            rating=data['rating'],
            comment=data['comment']
        )
    
    rating = product_instance.reviews.aggregate(Avg_rating=Avg('rating'))
    product_instance.rating = rating['Avg_rating']
    product_instance.save()
    
    return Response({'detail': 'Success'}, status=status.HTTP_200_OK)
