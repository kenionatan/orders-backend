from rest_framework import viewsets
from orders.models.client import Client
from orders.models.product import Product
from orders.models.order import Order
from orders.models.order_item import OrderItem
from .serializers import (ClientSerializer, ProductSerializer,
                          OrderSerializer, OrderItemSerializer)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
