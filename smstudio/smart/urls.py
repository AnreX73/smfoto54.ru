from django.urls import path

from smart.views import *

urlpatterns = [
    path('', index, name='home'),
    path('services/', services, name='services'),
    path('souvenirs/', souvenirs, name='souvenirs'),
    path('contacts/', contacts, name='contacts'),
    path('show_service/<slug:service_slug>', show_service, name='show_service'),
    path('alt_show_service/<slug:service_slug>', alt_show_service, name='alt_show_service'),

 ]