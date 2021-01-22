from django.db import models
from django.db.models import BooleanField, CharField, ImageField, TextField


class Photographer(models.Model):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    bio = TextField(max_length=1000)
    photo = ImageField(upload_to='images/%Y/%m/%d/')
    is_active = BooleanField(default=False)
