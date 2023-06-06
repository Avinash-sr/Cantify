from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartSerializer
from .models import *

@api_view(['POST', 'GET'])
def handlingCart(request):
    if request.method == 'GET':
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        enrollment_no = request.data.get('enrollment_no')
        item_id = request.data.get('item_id')
        quantity = request.data.get('quantity')
        
        try:
            profile = Profile.objects.get(enrollment_no=enrollment_no)
        except Profile.DoesNotExist:
            return Response({'error': 'Invalid enrollment number'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return Response({'error': 'Invalid item ID'}, status=status.HTTP_400_BAD_REQUEST)
        
        cart_data = {
            'profile': profile.enrollment_no,
            'item': item.id,
            'quantity': quantity
        }
        
        serializer = CartSerializer(data=cart_data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST','GET'])
# def handlingCart(request):
#     if request.method == 'GET':
#         carts = Cart.objects.all()
#         serializer = CartSerializer(carts, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         profile_data = request.data.get('profile')
#         item_data = request.data.get('item')
#         user_id = request.data.get('user')
#         quantity = request.data.get('quantity')

#         try:
#             profile = Profile.objects.get(enrollment_no=profile_data['enrollment_no'])
#         except Profile.DoesNotExist:
#             return Response({'error': 'Invalid enrollment number'}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             item = Item.objects.get(id=item_data['id'])
#         except Item.DoesNotExist:
#             return Response({'error': 'Invalid item ID'}, status=status.HTTP_400_BAD_REQUEST)

#         cart_data = {
#             'profile': profile.enrollment_no,
#             'item': item.id,
#             'user': user_id,
#             'quantity': quantity
#         }

#         serializer = CartSerializer(data=cart_data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


