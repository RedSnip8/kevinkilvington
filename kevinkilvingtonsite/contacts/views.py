from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
    if request.method == 'POST':
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        email = request.POST['email_address']
        phone = request.POST['phone_number']
        notes = request.POST['client_notes']
        current_page = request.POST['page']

        contact = Contact(
            f_name=first_name, l_name=last_name, email_address=email, 
            phone_number=phone, client_notes=notes 
        )

        contact.save

    #send_mail(
    #   'Customer Contact Request',
    #    f_name + l_name + 'has requested that you reach out to them.' + '"' + client_notes + '"',
    #    'request@kevinkilvington.com',
    #    ['kevin@kevinkilvington.com'],
    #    fail_silently=False,
    #)

        return redirect('/'+ current_page )