# shoppings_list/urlspy

from django.contrib import admin
from django.urls import path, include

from shopping_list.api.viewsets import ShoppingItemViewSet

from rest_framework import routers


router = routers.DefaultRouter()
router.register('shopping-items', ShoppingItemViewSet,
                basename='shopping-items')

urlpatterns = [
    path('api/', include(router.urls)),
]
