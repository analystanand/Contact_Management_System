from django.conf.urls import url
from django.urls import path,re_path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('contact/add_new/', views.add_new, name='add_new'),
    path('contact/add_new_count/', views.add_new_count, name='add_new_count'),
    path('contact/edit_contact/<int:pk>/', views.edit_contact, name='edit_contact'),
    path('contact/delete_contact/<int:pk>/', views.delete_contact, name='delete_contact'),
    path('contact/search/', views.search, name='search'),
    ]
