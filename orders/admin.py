from django.contrib import admin
from orders.models.product import Product
from orders.models.client import Client


admin.site.register(Product)
admin.site.register(Client)
