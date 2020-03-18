from django import forms

from .models import Contact, Address, Phone, Date


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['Fname', 'Mname', 'Lname']


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['Address_type', 'Street', 'City', 'State', 'Zip']


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['Phone_type', 'Area_code', 'Number']


class DateInput(forms.DateInput):
    input_type = 'date'


class DateForm(forms.ModelForm):
    class Meta:
        model = Date
        fields = ['Date_type', 'Date']
        widgets = {'Date': DateInput()}
