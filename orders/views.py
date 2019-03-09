from orders.models.product import Product
from django.views.generic import (
    ListView
)


class ListProducts(ListView):
    model = Product
