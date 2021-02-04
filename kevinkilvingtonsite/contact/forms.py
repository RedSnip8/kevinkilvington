from django import forms
from django.forms import CharField, EmailField, Textarea
from django.forms.widgets import EmailInput, TextInput

class ContactForm(forms.Form):
    f_name = CharField(label='Your First Name', max_length=100, widget=TextInput(attrs={'class': 'form-control'}))
    l_name = CharField(label='Your Last Name', max_length=200, widget=TextInput(attrs={'class': 'form-control'}))
    email_address = EmailField(label='Your Email Address', widget=EmailInput(attrs={'class': 'form-control'}))
    phone_number = CharField(label='Your Phone Number', max_length=10, widget=TextInput(attrs={'class': 'form-control'}))
    client_notes = CharField(label='Notes for Request', widget=Textarea(attrs={'required': False, 'class': 'form-control'}))