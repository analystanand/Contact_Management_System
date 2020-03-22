from csv import DictReader
from datetime import datetime
import numpy as np

from django.core.management import BaseCommand

from contact_app.models import Contact, Address, Phone, Date
from pytz import UTC
import re

DATETIME_FORMAT = '%Y-%m-%d'

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the contact data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from Contacts.csv into our Contact model"

    def handle(self, *args, **options):
        if Contact.objects.exists() or Phone.objects.exists():
            print('Contact data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Loading data for contact available for adoption")
        for row in DictReader(open('./Contacts.csv')):
            contact_obj = Contact()
            contact_obj.Fname = row['first_name']
            contact_obj.Mname = row['middle_name']
            contact_obj.Lname = row['last_name']
            contact_obj.save()

            if row["home_phone"]:
                phone_obj = Phone()
                phone_obj.Contact_id = contact_obj
                phone_pattern = row["home_phone"].replace("-", "")
                match1 = re.search(r'^([0-9]{3})', phone_pattern)
                match2 = re.search(r'([0-9]{7}$)', phone_pattern)
                phone_obj.Area_code = int(match1.group())
                phone_obj.Number = int(match2.group())
                phone_obj.Phone_type = "home_phone"
                phone_obj.save()

            if row["cell_phone"]:
                phone_obj = Phone()
                phone_obj.Contact_id = contact_obj
                phone_pattern = row["cell_phone"].replace("-", "")
                match1 = re.search(r'^([0-9]{3})', phone_pattern)
                match2 = re.search(r'([0-9]{7}$)', phone_pattern)
                phone_obj.Area_code = int(match1.group())
                phone_obj.Number = int(match2.group())
                phone_obj.Phone_type = "cell_phone"
                phone_obj.save()

            if row["work_phone"]:
                phone_obj = Phone()
                phone_obj.Contact_id = contact_obj
                phone_pattern = row["work_phone"].replace("-", "")
                match1 = re.search(r'^([0-9]{3})', phone_pattern)
                match2 = re.search(r'([0-9]{7}$)', phone_pattern)
                phone_obj.Area_code = int(match1.group())
                phone_obj.Number = int(match2.group())
                phone_obj.Phone_type = "work_phone"
                phone_obj.save()

            address_obj = Address()
            home_street = None
            home_city = None
            home_state = None
            home_zip = None

            if row['home_address']:
                home_street = row["home_address"]
            if row['home_city']:
                home_city = row["home_address"]
            if row['home_state']:
                home_state = row['home_state']
            if row['home_zip']:
                home_zip = row['home_zip']

            if home_street or home_city or home_state or home_zip:
                address_obj.Contact_id = contact_obj
                address_obj.Address_type = "home"
                address_obj.City = home_street
                address_obj.State = home_state
                address_obj.State = home_zip

            work_address_obj = Address()
            work_street = None
            work_city = None
            work_state = None
            work_zip = None

            if row['work_address']:
                work_street = row["work_address"]
            if row['work_city']:
                work_city = row["work_city"]
            if row['work_state']:
                work_state = row['work_state']
            if row['work_zip']:
                work_zip = row['work_zip']

            if work_street or work_city or work_state or work_zip:
                address_obj.Contact_id = contact_obj
                address_obj.Address_type = "work"
                address_obj.City = work_city
                address_obj.State = work_state
                address_obj.State = work_zip

            if row['birth_date']:
                date_obj = Date()
                date_obj.Contact_id= contact_obj
                raw_date = row['birth_date']
                bday_date = UTC.localize(
                    datetime.strptime(raw_date, DATETIME_FORMAT))
                date_obj.Date_type = "Birthday"
                date_obj.Date = bday_date
                date_obj.save()
