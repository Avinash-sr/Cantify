from django.urls import path, include
from . import views
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('order', OrderViewSet, basename='order')
router.register('cart', CartViewSet, basename='c')
urlpatterns = [
    # path('cartview/', views.handlingCart, name='cart'),
    # path('cartview/<int:pk>', views.cartAlter, name='cartAlter'),
    path('api/', include(router.urls)),
]