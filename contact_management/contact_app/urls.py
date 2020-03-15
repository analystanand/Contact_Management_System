from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    url(r'^contact/?(\d+)/', views.contact_detail, name='contact_detail')
    ]
