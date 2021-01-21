from django.db import models
from django.db.models import BooleanField, CharField, ImageField 

class Picture(models.Model):
    client_name = CharField(max_length=100, blank=True)
    photo_name = CharField(max_length=50, blank=True)
    photo_description = CharField( max_length=500, blank=True)
    photo_img = ImageField(upload_to='images/%Y/%m/%d/')
    on_grid = BooleanField(default=False)

