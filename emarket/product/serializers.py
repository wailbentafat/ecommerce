from rest_framework import serializers
from .models import product
class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'