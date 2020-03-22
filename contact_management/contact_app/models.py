from django.db import models
from localflavor.us.models import USStateField, USZipCodeField


class Contact(models.Model):
    Contact_id = models.AutoField(primary_key=True)
    Fname = models.CharField(max_length=50)
    Mname = models.CharField(max_length=50,blank=True)
    Lname = models.CharField(max_length=50)

    def __str__(self):
        return self.Fname


class Address(models.Model):
    Address_id = models.AutoField(primary_key=True)
    Contact_id = models.ForeignKey('Contact', on_delete=models.CASCADE,db_column="Contact_id")
    Address_type = models.CharField(max_length=50,null=True)
    Street = models.CharField(max_length=100,blank=True,null=True)
    City = models.CharField(max_length=50,blank=True,null=True)
    State = models.CharField(max_length=50,blank=True,null=True)
    Zip = models.IntegerField(blank=True,null=True)


class Phone(models.Model):
    Phone_id = models.AutoField(primary_key=True)
    Contact_id = models.ForeignKey('Contact', on_delete=models.CASCADE,db_column="Contact_id")
    Phone_type = models.CharField(max_length=50,blank=True,null=True)
    Area_code = models.IntegerField(blank=True,null=True)
    Number = models.IntegerField(blank=True,null=True)


class Date(models.Model):
    Date_id = models.AutoField(primary_key=True)
    Contact_id = models.ForeignKey('Contact', on_delete=models.CASCADE,db_column="Contact_id")
    Date_type = models.CharField(max_length=50,blank=True)
    Date = models.DateTimeField(blank=True,null=True)
