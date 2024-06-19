# serializers.py
from rest_framework import serializers
from .models import product, review

class reviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = review
        fields = '__all__'

class productSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField(method_name='get_reviews', read_only=True)
    
    class Meta:
        model = product
        fields = '__all__'
        
    def get_reviews(self, obj):
        reviews = obj.reviews.all()
        serializer = reviewSerializer(reviews, many=True)
        return serializer.data
