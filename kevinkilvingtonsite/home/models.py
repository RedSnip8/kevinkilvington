from django.db import models
from django.db.models import BooleanField, CharField, ImageField
from django.db.models.fields.related import ForeignKey
from albums.models import Album


class Picture(models.Model):
    client_name = CharField(max_length=100, blank=True)
    photo_name = CharField(max_length=50, blank=True)
    photo_album = ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True)
    photo_img = ImageField(upload_to='images/%Y/%m/%d/')
    on_grid = BooleanField(default=False)
