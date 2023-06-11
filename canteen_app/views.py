from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer