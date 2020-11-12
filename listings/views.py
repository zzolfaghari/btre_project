from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'listing/listings.html')


def listing(request):
    return render(request, 'listing/listing.html')


def search(request):
    return render(request, 'listing/search.html')
