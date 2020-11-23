from django.shortcuts import render
from django.http import HttpResponse
from .models import Listing


def index(request):
    listings = Listing.objects.all()
    context = {'listings': listings}
    return render(request, 'listing/listings.html', context)


def listing(request):
    return render(request, 'listing/listing.html')


def search(request):
    return render(request, 'listing/search.html')
