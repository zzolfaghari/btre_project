from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse
from .models import Listing


def index(request):
    listings = Listing.objects.all()
    paginator = Paginator(Listing, 4)  # Show 4 listings per page.

    page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    context = {'listings': listings}
    return render(request, 'listing/listings.html', context)


def listing(request, listing_id):
    return render(request, 'listing/listing.html')


def search(request):
    return render(request, 'listing/search.html')
