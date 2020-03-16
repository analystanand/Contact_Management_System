from django import forms
from .models import Contact, Address, Phone, Date

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('Fname', 'Mname','Lname')
