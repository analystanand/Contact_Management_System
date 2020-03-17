from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .models import Contact, Address, Phone, Date
from .forms import ContactForm, AddressForm, PhoneForm, DateForm
from django.http import Http404, HttpResponseRedirect


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
        filled_contact_form = ContactForm(request.POST)
        filled_address_form = AddressForm(request.POST)
        filled_phone_form = PhoneForm(request.POST)
        filled_date_form = DateForm(request.POST)

        valid_contact = filled_contact_form.is_valid()
        valid_address = filled_address_form.is_valid()
        valid_phone = filled_phone_form.is_valid()
        valid_date = filled_date_form.is_valid()

        if valid_contact and valid_address and valid_phone and valid_date:
            created_contact = filled_contact_form.save()

            temp_address = filled_address_form.save(commit=False)
            temp_phone = filled_phone_form.save(commit=False)
            temp_date = filled_date_form.save(commit=False)

            temp_address.Contact_id = created_contact
            temp_phone.Contact_id = created_contact
            temp_date.Contact_id = created_contact

            temp_address.save()
            temp_phone.save()
            temp_date.save()
            return redirect('contact_detail', pk=created_contact.pk)
    else:
        contact_form_obj = ContactForm()
        address_form_obj = AddressForm()
        phone_form_obj = PhoneForm()
        date_form_obj = DateForm()
        return render(request, 'add_new.html', {"contact": contact_form_obj,
                                                "address": address_form_obj,
                                                "phone": phone_form_obj,
                                                "date": date_form_obj})


def edit_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    address = Address.objects.get(Contact_id=pk)
    phone = Phone.objects.get(Contact_id=pk)
    date = Date.objects.get(Contact_id=pk)

    # pre fill data from previous information
    pre_filled_contact_form = ContactForm(contact)
    pre_filled_address_form = AddressForm(address)
    pre_filled_phone_form = PhoneForm(phone)
    pre_filled_date_form = DateForm(date)

    if request.method == "POST":
        filled_contact_form = ContactForm(request.POST, instance=contact)
        filled_address_form = AddressForm(request.POST, instance=address)
        filled_phone_form = PhoneForm(request.POST, instance=phone)
        filled_date_form = DateForm(request.POST, date)

        valid_contact = filled_contact_form.is_valid()
        valid_address = filled_address_form.is_valid()
        valid_phone = filled_phone_form.is_valid()
        valid_date = filled_date_form.is_valid()

        if valid_contact and valid_address and valid_phone and valid_date:
            filled_contact_form.save()
            filled_address_form.save()
            filled_phone_form.save()
            filled_date_form.save()

            contact_form = filled_contact_form
            address_form = filled_address_form
            phone_form = filled_phone_form
            date_form = filled_date_form

            return HttpResponseRedirect(reversed(''))
        else:
            return render(request, 'edit_contact.html', {"contact": pre_filled_contact_form,
                                                         "address": pre_filled_address_form,
                                                         "phone": pre_filled_phone_form,
                                                         "date": pre_filled_date_form})

    else:
        return render(request, 'edit_contact.html', {"contact": pre_filled_contact_form,
                                                     "address": pre_filled_address_form,
                                                     "phone": pre_filled_phone_form,
                                                     "date": pre_filled_date_form})
