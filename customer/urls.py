from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('cart/', views.handlingCart, name='cart'),
]