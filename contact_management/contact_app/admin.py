from django.contrib import admin
from .models import Contact,Phone,Address,Date

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
     list_display = ['Fname','Lname']

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['Contact_id']
    pass

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['Contact_id']
    pass

@admin.register(Date)
class DateAdmin(admin.ModelAdmin):
    list_display = ['Contact_id']
    pass