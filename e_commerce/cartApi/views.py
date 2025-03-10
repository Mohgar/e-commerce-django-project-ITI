from rest_framework import viewsets
from .models import Cart, CartItem
from .serializers import CartItemSerializer, CartSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import AdminDeletePermission

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes=[IsAuthenticated, AdminDeletePermission]

# Create your views here.
