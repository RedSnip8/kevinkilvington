from django.db import models
from django.db.models import BooleanField, CharField, ImageField
from django.db.models.fields.related import ForeignKey


class Picture(models.Model):
    client_name = CharField(max_length=100, blank=True)
    photo_name = CharField(max_length=50, blank=True)
    photo_album = ForeignKey('albums.Album', on_delete=models.CASCADE, blank=True, null=True)
    event_name = ForeignKey('albums.Events', on_delete=models.CASCADE, blank=True, null=True)
    photo_alt_text = CharField(max_length=200, blank=True)
    photo_img = ImageField(upload_to='images/%Y/%m/%d/')
    on_grid = BooleanField(default=False)
    album_cover = BooleanField(default=False)
