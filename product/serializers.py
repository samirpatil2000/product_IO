from rest_framework import serializers
from .models import Product,ProductInCart,Order
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','name','price','desc']

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=100)
    password = serializers.CharField(required=True,max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields =['products_in_cart','user','is_completed','purchase_date']


