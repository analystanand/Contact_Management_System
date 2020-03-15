from django.db import models
from django.core.validators import MaxValueValidator
from localflavor.us.models import USStateField, USZipCodeField


class Contact(models.Model):
    Contact_id = models.AutoField(primary_key=True)
    Fname = models.CharField(max_length=50)
    Mname = models.CharField(max_length=50)
    Lname = models.CharField(max_length=50)

    def __str__(self):
        return self.Fname


class Address(models.Model):
    Address_id = models.AutoField(primary_key=True)
    Contact_id = models.ForeignKey('Contact', on_delete=models.CASCADE)
    Address_type = models.CharField(max_length=50)
    Street = models.CharField(max_length=200)
    City = models.CharField(max_length=100)
    State = USStateField()
    Zip = USZipCodeField(blank=True)


class Phone(models.Model):
    Phone_id = models.AutoField(primary_key=True)
    Contact_id = models.ForeignKey('Contact', on_delete=models.CASCADE)
    Phone_type = models.CharField(max_length=50)
    Area_code = models.IntegerField(validators=[MaxValueValidator(999)])
    Number = models.IntegerField()


class Date(models.Model):
    Date_id = models.AutoField(primary_key=True)
    Contact_id = models.ForeignKey('Contact', on_delete=models.CASCADE)
    Date_type = models.CharField(max_length=50)
    Date = models.DateTimeField()
