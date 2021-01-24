from django.db import models
from django.db.models import CharField
from django.db.models.fields import BooleanField, CharField

class Album(models.Model):
    Album_name = CharField(max_length=100)
    is_active = BooleanField(default=True)

    def __str__(self) -> str:
        return self.Album_name