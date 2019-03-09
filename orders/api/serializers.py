from rest_framework import serializers
from orders.models.client import Client
from orders.models.product import Product


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'client_name')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'product_title', 'product_price', 'product_multiple')
