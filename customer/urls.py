from django.urls import path
from .views import *

urlpatterns = [
    path('cart_item/', CartItemView.as_view(), name='cart-item'),
    path('order/', OrderView.as_view(), name='order'),
]