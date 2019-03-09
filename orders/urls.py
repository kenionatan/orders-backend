from django.urls import path
from .views import (
    ListProducts
)

urlpatterns = [
    path('product_list', ListProducts.as_view()),

]
