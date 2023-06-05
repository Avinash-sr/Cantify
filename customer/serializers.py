from rest_framework import serializers
from .models import *
from canteen_app.serializers import ItemSerializer

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    item = ItemSerializer()

    class Meta:
        model = Cart
        fields = '__all__'
