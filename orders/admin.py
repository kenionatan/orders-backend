from django.contrib import admin
from orders.models.product import Product
from orders.models.client import Client
from orders.models.order import Order
from orders.models.order_item import OrderItem


admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(OrderItem)
