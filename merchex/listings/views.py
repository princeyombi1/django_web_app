from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing
from django.shortcuts import render

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands' : bands})

def about(request):
    return render(request, 'listings/about.html')

def contact(request):
    return render(request, 'listings/contact.html')

