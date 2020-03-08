from django.db import models
from django.core.validators import MaxValueValidator
from localflavor.us.models import USStateField, USZipCodeField


class Contact(models.Model):
    Contact_id = models.AutoField(primary_key=True)
    Fname = models.CharField(max_length=100, )
    Mname = models.CharField(max_length=100)
    Lname = models.CharField(max_length=100)


class Address(models.Model):
    ADDRESS_TYPE_CHOICE = [('H', 'Home'), ('W', 'Work'), ('O', 'Other')]
    Address_id = models.AutoField(primary_key=True)
    Contact_id = models.ForeignKey('Contact', on_delete=models.CASCADE)
    Address_type = models.CharField(choices=ADDRESS_TYPE_CHOICE)
    Street_Address = models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    State = USStateField()
    Zip = USZipCodeField(blank=True)


class Phone(models.Model):
    PHONE_TYPE_CHOICE = [('H', 'Home'), ('W', 'Work'), ('O', 'Other')]
    Phone_id = models.AutoField(primary_key=True)
    Contact_id = models.ForeignKey('Contact', on_delete=models.CASCADE)
    Phone_type = models.CharField(choices=PHONE_TYPE_CHOICE)
    Area_code = models.IntegerField(validators=[MaxValueValidator(999)])
    Number = models.IntegerField()


class Date(models.Model):
    DATE_TYPE_CHOICE = [('H', 'Birthday'), ('W', 'Anniversary'), ('O', 'Other')]
    Date_id = models.AutoField(primary_key=True)
    Contact_id = models.ForeignKey('Contact', on_delete=models.CASCADE)
    Date_type = models.CharField(choices=DATE_TYPE_CHOICE)
    Date = models.DateTimeField()
