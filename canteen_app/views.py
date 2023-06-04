from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.
class ItemListAPIView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer