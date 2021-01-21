from django.db import models
from django.db.models import BooleanField, CharField, DecimalField


class Services(models.Model):
    service_name = CharField(max_length=100)
    service_description = CharField(max_length=1000)
    price = DecimalField(max_digits=6, decimal_places=2)
    is_availible = BooleanField(default=True)