from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator

from django.db.models.fields import CharField, DateTimeField, EmailField, TextField

class Contact(models.Model):
    f_name = CharField(max_length=100)
    l_name = CharField(max_length=200)
    email_address = EmailField(blank=True)
    phone_number = CharField(max_length=10)
    client_notes = TextField(blank=True)
    request_date = DateTimeField(default=datetime.now, blank=True)
