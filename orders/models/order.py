from django.db import models
from .client import Client
from django.utils import timezone


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=None)
    grand_total = models.FloatField(default=0)
    create_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return Client.client_name
