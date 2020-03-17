from django.conf.urls import url
from django.urls import path,re_path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # url(r'^contact/?(\d+)/', views.contact_detail, name='contact_detail')
    path('contact/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('contact/add_new/', views.add_new, name='add_new'),
    ]
