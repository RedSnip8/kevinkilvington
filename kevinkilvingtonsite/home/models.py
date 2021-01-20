from django.db import models
from django.db.models.fields import BooleanField

class Picture(models.Model):
    client_name = models.CharField(max_length=100, blank=True)
    photo_name = models.CharField(max_length=50, blank=True)
    photo_description = models.CharField( max_length=500, blank=True)
    photo_img = models.ImageField(upload_to='images/%Y/%m/%d/')
    on_grid = BooleanField(default=False)

