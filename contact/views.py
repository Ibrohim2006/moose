from django.shortcuts import render, redirect
from .models import *
from .utils import send_message_telegram


def contact_view(request):
    if request.method == 'POST':
        data = request.POST
        contact = Contact.objects.create(first_name=data.get('first_name'), last_name=data.get('last_name'),
                                         phone_number=data.get('phone_number'),
                                         message=data.get('message'), email=data.get('email'))
        contact.save()
        send_message_telegram(contact)
        return redirect('/contact')
    return render(request, 'contact.html')
