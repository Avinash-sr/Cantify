from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('item', ItemViewSet, basename='item')
urlpatterns = [
   path('item/', include(router.urls)),
]