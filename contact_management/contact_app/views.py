from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact,Address,Phone,Date
from django.http import Http404



def home(request):
    contacts = Contact.objects.all()
    return render(request,'home.html',{'contacts':contacts})


def contact_detail(request, id):
    try:
        cont_obj = Contact.objects.get(Contact_id=id)
        address_obj = Address.objects.filter(Contact_id=id)
        phone_obj = Phone.objects.filter(Contact_id=id)
        date_obj = Date.objects.filter(Contact_id=id)
        result = {'contact':cont_obj,"address":address_obj,"phone":phone_obj,"date":date_obj}
    except Contact.DoesNotExist:
        raise Http404('Contact not found')
    return render(request,'contact.html',result)
