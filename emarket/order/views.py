
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated,isAdminUser
from rest_framework import status
from django.db.models import Avg
from .models import Order, OrderItem
from .serializers import productSerializer
from product.models import product
from .serializers import orderserializer, orderitemserializer
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def new_order(request):
    user=request.user
    data=request.data
    order_item=data['order_items']
    if order_item and len(order_item) == 0:
        return Response({"error": "No order items"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        total_amount=sum([item['price'] * item['quantity'] for item in order_item])
        order=Order.object.create(
            user=user,
            total_amount=total_amount,
            payement_method=data['payement_method'],
            address=data['address'],
            city=data['city'],
            street=data['street'],
            phone_number=data['phone_number'],
            postal_code=data['postal_code']
        )
        for i in order_item:
            product_instance=get_object_or_404(product, id=i['product_id'])
            product_instance=OrderItem.objects.create(
                order=order,
                product=product_instance,
                quantity=i['quantity'],
                name=i['name'],
                price=i['price']
            )
            product.stock-=i['quantity']
            product.save()
            serializer=orderserializer(order, many=False)
            return Response({"order": serializer.data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_orders(request):
    user=request.user
    orders=Order.objects.filter(user=user)
    serializer=orderserializer(orders, many=True)
    return Response({"orders": serializer.data})




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_order(request,pk):
    user=request.user
    orders=Order.objects.filter(user=user ,id=pk)
    serializer=orderserializer(orders, many=False)
    return Response({"orders": serializer.data})



@api_view(['PUT'])
@permission_classes([IsAuthenticated,isAdminUser])
def get_orders(request,pk):
    user=request.user
    order=Order.objects.filter(user=user,id=pk)
    order.statue=request.data['statue']
    order.save()
    serializer=orderserializer(order, many=True)
    return Response({"orders": serializer.data})

