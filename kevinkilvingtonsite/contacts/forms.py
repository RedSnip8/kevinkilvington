from django import forms
from django.forms import CharField, EmailField, Textarea

class ContactForm(forms.Form):
    f_name = CharField(label='Your First Name', max_length=100)
    l_name = CharField(label='Your Last Name', max_length=200)
    email_address = EmailField(label='Your Email Address')
    phone_number = CharField(label='Your Phone Number', max_length=10)
    client_notes = CharField(label='Notes for Request', widget=Textarea(attrs={'required': False}))