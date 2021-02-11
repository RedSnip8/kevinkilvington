from django.db import models
from django.db.models import CharField
from django.db.models.fields import BooleanField, CharField, DateTimeField

class Album(models.Model):
    Album_name = CharField(max_length=100)
    is_active = BooleanField(default=True)

    def __str__(self) -> str:
        return self.Album_name

class Events(models.Model):
    event_name = CharField(max_length=200)
    event_year = CharField(max_length=4)
    is_active = BooleanField(default=True)

    def __str__(self) -> str:
        return self.event_name