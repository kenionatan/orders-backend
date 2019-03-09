from rest_framework import serializers
from orders.models.client import Client
from orders.models.product import Product
from orders.models.order import Order
from orders.models.order_item import OrderItem


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'client_name')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'product_title', 'product_price', 'product_multiple')


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product', 'price',
                  'quantityProduct', 'profitability')


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'client', 'quantityItem', 'grand_total',
                  'items', 'create_date', 'update_date')
