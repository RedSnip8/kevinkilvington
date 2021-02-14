from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.utils import timezone
from django.contrib import messages
from django.template.loader import render_to_string


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

            msg_to_k_plain = render_to_string('contact/newcontact.txt', {"newcontact": new_contact})
            msg_to_k_html = render_to_string('contact/newcontact.html', {"newcontact": new_contact})
            msg_to_c_plain = render_to_string('contact/confirmation.txt', {"newcontact": new_contact})
            msg_to_c_html = render_to_string('contact/confirmation.html', {"newcontact": new_contact})

            try:
            
                send_mail(
                'Customer Contact Request',
                msg_to_k_plain,
                'info.donotreply@kevinkilvington.com',
                ['kevin@kevinkilvington.com'],
                html_message=msg_to_k_html,
                fail_silently=False,
                )

                send_mail(
                    'Thank you for your request!',
                    msg_to_c_plain,
                    'info.donotreply@kevinkilvington.com',
                    [new_contact.email_address],
                    html_message=msg_to_c_html,
                    fail_silently=False,
                )
            except BadHeaderError:
                messages.warning(request, 'Invailid Header Found')
                return HttpResponseRedirect('/contact', {'new_contact': new_contact})

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
