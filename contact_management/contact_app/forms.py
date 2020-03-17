from django import forms

from .models import Contact, Address, Phone, Date


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['Contact_id','Fname', 'Mname', 'Lname']
        widgets = {'Contact_id': forms.HiddenInput()}


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['Contact_id','Address_type', 'Street', 'City', 'State', 'Zip']
        widgets = {'Contact_id': forms.HiddenInput()}


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['Contact_id','Phone_type', 'Area_code', 'Number']
        widgets = {'Contact_id': forms.HiddenInput()}


class DateInput(forms.DateInput):
    input_type = 'date'

class DateForm(forms.ModelForm):
    class Meta:
        model = Date
        fields = ['Contact_id','Date_type', 'Date']
        widgets = {'Contact_id': forms.HiddenInput(),'Date':DateInput()}