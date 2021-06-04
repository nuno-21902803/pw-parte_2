#  website/urls.py

from django.urls import path
from django.shortcuts import render
from . import views


app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('details/<int:productId>', views.details_page_view, name='details'),
    path('contacts', views.contacts_page_view, name='contacts')
]