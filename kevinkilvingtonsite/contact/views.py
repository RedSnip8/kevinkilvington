from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib import messages

from .models import Contact

from .forms import ContactForm

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            new_contact = Contact(
            f_name = form.cleaned_data['f_name'],
            l_name = form.cleaned_data['l_name'],
            email_address = form.cleaned_data['email_address'],
            phone_number = form.cleaned_data['phone_number'],
            client_notes = form.cleaned_data['client_notes'],
            request_date = timezone.now(),         
            )
            new_contact.save()

            
            messages.success(request, 'Thank you, I will reach out to you as soon as I can!')
            return HttpResponseRedirect('/contact', {'new_contact': new_contact})

    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})

    



'''
def contact(request):
    print(request)
    if request.method == 'POST':
        print("test")
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

    send_mail(
       'Customer Contact Request',
        f_name + l_name + 'has requested that you reach out to them.' + '"' + client_notes + '"',
        'request@kevinkilvington.com',
        ['kevin@kevinkilvington.com'],
        fail_silently=False,
    )

        return redirect('/'+ current_page )

    elif request.method == 'GET':
        print('poop')
        return redirect('/')
'''
