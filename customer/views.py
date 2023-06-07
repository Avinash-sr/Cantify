from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
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
        user = profile.user
        cartItem=Cart.objects.create(item=item,user=user,quantity=quantity)
        
        cartItem.save()
        return Response(CartSerializer(cartItem).data)
    