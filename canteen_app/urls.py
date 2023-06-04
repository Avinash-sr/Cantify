from django.urls import path
from .views import *

urlpatterns = [
    path('items/', ItemListAPIView.as_view(), name='item_list'),
]