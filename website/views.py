#  config/views.py

from django.shortcuts import render
from datetime import datetime


def home_page_view(request):
    context = {'now': datetime.now()}
    return render(request, 'website/home.html', context)


def details_page_view(request, productId):
    #Query to search product with the path parameter
    return render(request, 'website/details.html', {'productId': productId})


def contacts_page_view(request):
    return render(request, 'website/contacts.html')
