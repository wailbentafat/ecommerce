from rest_framework import serializers
from .models import Order, OrderItem
from product.models import product
from django.contrib.auth.models import User

class orderserializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
class orderitemserializer(serializers.ModelSerializer):
    orderitem=serializers.SerializerMethodField(method_name='get_orderitem', read_only=True)
    class Meta:
        model = OrderItem
        fields = '__all__'       
    def get_orderitem(self, obj):
        orderitem = obj.order_items.all()    
        serializer=orderitemserializer(order_items
                                       , many=True)
        return serializer.data