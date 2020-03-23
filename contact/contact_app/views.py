import re
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.forms import formset_factory
from .models import Contact, Address, Phone, Date
from .forms import ContactForm, AddressForm, PhoneForm, DateForm, MultipleForm


def home(request):
    contact_list = Contact.objects.all().order_by('Contact_id')
    paginator = Paginator(contact_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj})


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


def add_new_count(request):
    forms_count = {'no_of_addresses': 1, 'no_of_phones': 1, 'no_of_dates': 1}
    multiple_form = MultipleForm(initial=forms_count)
    return render(request, 'add_new_count.html', {'multiple_form': multiple_form})


def add_new(request):
    forms_count = {'no_of_addresses': 0, 'no_of_phones': 0, 'no_of_dates': 0}
    filled_multiple_form = MultipleForm(request.GET)
    if filled_multiple_form.is_valid():
        forms_count['no_of_addresses'] = filled_multiple_form.cleaned_data['no_of_addresses']
        forms_count['no_of_phones'] = filled_multiple_form.cleaned_data['no_of_phones']
        forms_count['no_of_dates'] = filled_multiple_form.cleaned_data['no_of_dates']
    else:
        HttpResponseRedirect(('add_new_count'))

    contact_form_obj = ContactForm()
    address_form_obj = formset_factory(AddressForm, extra=forms_count['no_of_addresses'])
    phone_form_obj = formset_factory(PhoneForm, extra=forms_count['no_of_phones'])
    date_form_obj = formset_factory(DateForm, extra=forms_count['no_of_dates'])

    if request.method == 'POST':
        filled_contact_form = ContactForm(request.POST)
        filled_address_form_set = address_form_obj(request.POST)
        filled_phone_form_set = phone_form_obj(request.POST)
        filled_date_form_set = date_form_obj(request.POST)

        valid_contact = filled_contact_form.is_valid()
        valid_address = filled_address_form_set.is_valid()
        valid_phone = filled_phone_form_set.is_valid()
        valid_date = filled_date_form_set.is_valid()

        if valid_contact and valid_address and valid_phone and valid_date:
            created_contact = filled_contact_form.save()

            temp_address = [j.save(commit=False) for j in filled_address_form_set]
            temp_phone = [f.save(commit=False) for f in filled_phone_form_set]
            temp_date = [k.save(commit=False) for k in filled_date_form_set]

            for j in temp_address:
                j.Contact_id = created_contact
                j.save()

            for f in temp_phone:
                f.Contact_id = created_contact
                f.save()

            for k in temp_date:
                k.Contact_id = created_contact
                k.save()

            return redirect('contact_detail', pk=created_contact.pk)
        else:
            return HttpResponseRedirect('home')

    address_form_set = address_form_obj()
    phone_form_set = phone_form_obj()
    date_form_set = date_form_obj()

    return render(request, 'add_new.html', {"contact": contact_form_obj,
                                            "address": address_form_set,
                                            "phone": phone_form_set,
                                            "date": date_form_set})


def edit_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    address = Address.objects.filter(Contact_id=pk)
    phone = Phone.objects.filter(Contact_id=pk)
    date = Date.objects.filter(Contact_id=pk)

    #create multiple forms
    address_formset= formset_factory(AddressForm,extra=0)
    phone_formset = formset_factory(PhoneForm,extra=0)
    date_formset = formset_factory(DateForm, extra=0)

    if request.method == 'POST':
        filled_contact_form = ContactForm(request.POST)
        filled_address_formset = address_formset(request.POST)
        filled_phone_formset = phone_formset(request.POST)
        filled_date_formset = date_formset(request.POST)

        valid_contact = filled_contact_form.is_valid()
        valid_address = filled_address_formset.is_valid()
        valid_phone = filled_phone_formset.is_valid()
        valid_date = filled_date_formset.is_valid()

        if valid_contact and valid_address and valid_phone and valid_date:
            updated_contact = filled_contact_form.save()
            temp_address = [j.save(commit=False) for j in filled_address_formset]
            temp_phone = [f.save(commit=False) for f in filled_phone_formset]
            temp_date = [k.save(commit=False) for k in filled_date_formset]

            for j in temp_address:
                j.Contact_id = updated_contact
                j.save()

            for f in temp_phone:
                f.Contact_id = updated_contact
                f.save()

            for k in temp_date:
                k.Contact_id = updated_contact
                k.save()

        return redirect('contact_detail', pk=updated_contact.pk)

    address_value = list(address.values('Address_type','Street','City','State','Zip'))
    phone_value = list(phone.values('Phone_type','Area_code','Number'))
    date_value = list(date.values('Date_type','Date'))

    # pre fill data from previous information
    pre_filled_contact_form = ContactForm(instance=contact)
    pre_filled_address_formset = address_formset(initial=address_value)
    pre_filled_phone_formset = phone_formset(initial=phone_value)
    pre_filled_date_formset = date_formset(initial=date_value)

    return render(request, 'edit.html', {"contact": pre_filled_contact_form,
                                         "address": pre_filled_address_formset,
                                         "phone": pre_filled_phone_formset,
                                         "date": pre_filled_date_formset})


def delete_contact(request, pk):
    contact = get_object_or_404(Contact, Contact_id=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('home')
    else:
        return render(request, 'delete.html', {'contact': contact})


def normalize_search(search_term,
                     getterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                     normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in getterms(search_term)]


def search(request):
    search_term = ''
    fields = ['Fname', 'Mname', 'Lname',
              'address__Address_type', 'address__Street', 'address__City','address__State', 'address__Zip',
              'phone__Phone_type', 'phone__Area_code','phone__Number']
    contacts = Contact.objects.all()
    query = None
    if 'search' in request.GET:
        search_term = request.GET["search"]
        if search_term:
            terms = normalize_search(search_term)
            for t in terms:
                or_query = None
                for f in fields:
                    q = Q(**{"%s__icontains" % f: t})
                    or_query = q if or_query is None else or_query | q
                if query is None:
                    query = or_query
                else:
                    query = query | or_query

            contacts = contacts.filter(query).distinct()
    context = {'contacts': contacts, 'search_term': search_term}
    return render(request, 'search.html', context)
