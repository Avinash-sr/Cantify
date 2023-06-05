from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartSerializer
from .models import *

@api_view(['POST'])
def handlingCart(request):

    if request.method == 'GET':
        carts = Cart.objects.all()  # Assuming you have a Cart model
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        profile = request.user.profile
        user_id = profile.user_id
        user_obj = Profile.objects.filter(user_id=user_id)
        item_id = Item.id
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
