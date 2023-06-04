from rest_framework import serializers
from .models import *

class CartItemSerializer(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all)

    class Meta:
        model = CartItem
        fields = ['item', 'quantity']

class CartSerailizer(serializers.ModelSerializer):
    items = CartItemSerializer(many= True, read_only= True)

    class Meta:
        model= Cart
        fields = ['id', 'user', 'items'] 

class OrderItemSerializer(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())
    
    class Meta:
        model = OrderItem
        fields = ['item', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many= True, read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'items', 'created_at']