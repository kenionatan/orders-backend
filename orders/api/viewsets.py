from rest_framework import viewsets
from orders.models.client import Client
from orders.models.product import Product
from .serializers import (ClientSerializer, ProductSerializer)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
