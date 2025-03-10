from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet, CartItemViewSet

router = DefaultRouter()
router.register(r'my-cart', CartViewSet)
router.register(r'my-cart-items', CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]