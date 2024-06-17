from rest_framework import serializers
from .models import product,review

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'
        
class reviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = review
        fields = '__all__'