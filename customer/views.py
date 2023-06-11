from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from rest_framework import viewsets, generics

class OrderViewSet(viewsets.ModelViewSet):

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    
class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all() 

# @api_view(['POST', 'GET'])
# def handlingCart(request):
#     if request.method == 'GET':
#         carts = Cart.objects.all()
#         serializer = CartSerializer(carts, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         enrollment_no = request.data.get('enrollment_no')
#         item_id = request.data.get('item_id')
#         quantity = request.data.get('quantity')
        
#         try:
#             profile = Profile.objects.get(enrollment_no=enrollment_no)
#         except Profile.DoesNotExist:
#             return Response({'error': 'Invalid enrollment number'}, status=status.HTTP_400_BAD_REQUEST)
        
#         try:
#             item = Item.objects.get(id=item_id)
#         except Item.DoesNotExist:
#             return Response({'error': 'Invalid item ID'}, status=status.HTTP_400_BAD_REQUEST)
#         user = profile.user
#         cartItem=Cart.objects.create(item=item,user=user,quantity=quantity)
        
#         cartItem.save()
#         return Response(CartSerializer(cartItem).data)

# @api_view(['GET', 'DELETE'])
# def cartAlter(request,pk):

#     try:
#         cart = Cart.objects.get(pk=pk)
#     except Cart.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         cartSerializer = CartSerializer(cart)
#         return Response(cartSerializer.data)
    
#     elif request.method == 'DELETE':
#         cart.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
    # elif request.method == 'PUT':
    #     enrollment_no = request.data.get('enrollment_no')
    #     item_id = request.data.get('item_id')
    #     quantity = request.data.get('quantity')
        
    #     try:
    #         profile = Profile.objects.get(enrollment_no=enrollment_no)
    #     except Profile.DoesNotExist:
    #         return Response({'error': 'Invalid enrollment number'}, status=status.HTTP_400_BAD_REQUEST)
        
    #     try:
    #         item = Item.objects.get(id=item_id)
    #     except Item.DoesNotExist:
    #         return Response({'error': 'Invalid item ID'}, status=status.HTTP_400_BAD_REQUEST)
    #     user = profile.user
    #     cartSerializer = CartSerializer(cart, data=request.data)
    #     if cartSerializer.is_valid():
    #         cartSerializer.save()
    #         return Response(cartSerializer.data)
    #     return Response(cartSerializer.errors)