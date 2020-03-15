
1. Create virtual environment for web application
2. Install  django framework with pip `pip install django`
3. Create a project `django-admin.py startproject contact_management`
4. Test if project is working or not by running command on contact_managemet directory `python manage.py runserver`
5. Check `http://localhost:8000/` if it's loading django's default page or not
6. Create an app within project by executing cmd `python manage.py startapp contact_app`
7. Add 'contact_management' to under INSTALLED_APPS settings.py 
8. Create models for below given list: Contact, Address, Phone and Date
9. Create migration task by `python manage.py makemigrations`
10. Check pending migration by `python manage.py showmigrations
11. Add single record from contacts.csv
12. Add admin for Contact Model
13. Create super user 
14. add view and url pattern
15. add template

       