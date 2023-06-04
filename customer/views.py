from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.

class CartItemView(APIView):
    def get(self, request):
        # Logic for handling GET requests
        cart = Cart.objects.get(user=request.user)
        serializer = CartItemSerializer(cart.items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            cart = Cart.objects.get(user=request.user)
            item= serializer.validated_data['item']
            quantity = serializer.validated_data['quantity']

            cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
            if not created:
                cart_item.quantity += quantity
                cart_item.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderView(APIView):

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            cart = Cart.objects.get(user=request.user)
            order = Order.objects.create(user= request.user)

            for cart_item in cart.items.all():
                OrderItem.objects.create(order=order, item=cart_item.items, quantity = cart_item.quantity)

            cart.items.clear()

            return Response(serializer.data, status=status.HTTP_201_Created)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)