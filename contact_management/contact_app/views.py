from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Contact, Address, Phone, Date
from .forms import ContactForm, AddressForm, PhoneForm, DateForm
from django.http import Http404


def home(request):
    contacts = Contact.objects.all()
    return render(request, 'home.html', {'contacts': contacts})


def contact_detail(request, pk):
    try:
        cont_obj = Contact.objects.filter(Contact_id=pk)
        address_obj = Address.objects.filter(Contact_id=pk)
        phone_obj = Phone.objects.filter(Contact_id=pk)
        date_obj = Date.objects.filter(Contact_id=pk)
        result = {'contact': cont_obj, "address": address_obj, "phone": phone_obj, "date": date_obj}
    except Contact.DoesNotExist:
        raise Http404('Contact not found')
    return render(request, 'contact.html', result)


def add_new(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return redirect('contact_detail', pk=contact.pk)
    else:
        contact_form_obj = ContactForm()
        address_form_obj = AddressForm()
        phone_form_obj = PhoneForm()
        date_form_obj = DateForm()
        return render(request, 'add_new.html', {"contact": contact_form_obj,
                                                "address": address_form_obj,
                                                "phone": phone_form_obj,
                                                "date": date_form_obj})
