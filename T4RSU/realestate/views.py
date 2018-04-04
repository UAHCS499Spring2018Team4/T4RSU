from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from .models import Agency
from .models import Listing
from django.contrib.auth import authenticate
#from django.core.context_processors import csrf
from django.shortcuts import render

from . import (
    FeedbackView,
    ListingCreateView,
    ListingDeleteView,
    ListingEditView,
    ListingView,
    Overview,
    SearchView,
    ShowingEditView,
    ShowingScheduleView
)

def index(request):

    return HttpResponse("<h2>Hello World</h2>")



def demo(request):
    all_agencies = Agency.objects.all()
    template = loader.get_template('realestate/demo.html')
    context = {
        'all_agencies': all_agencies,
    }
    return HttpResponse(template.render(context, request))


def ListView(request):
    all_listings = Listing.objects.all()
    html = ''
    for listing in all_listings:
        url1 = '/realestate/' + str(listing.id) + '/del/'
        url2 = '/realestate/' + str(listing.id) + '/change/'
       # html += '<a href="' + url2 + '">' + str(listing.MLSNumber) + '</a><br>'
        html += '<a href="' + url1 + '">' + str(listing.MLSNumber) + '   </a>'
        html += '<a href="' + url2 + '">' + str(listing.MLSNumber) + '</a><br>'

    return HttpResponse(html)

def ListChange(request, listing_id):
    a = Listing.objects.get(id=listing_id)
    newMLSNumber = int("0101")
    a.MLSNumber = newMLSNumber
    a.save()

    url = '/realestate/ListView/'
    html = '<a href="' + url + '">' + "Return to list?" + '</a><br>'

    return HttpResponse("<h1>Listing ID " + str(listing_id) + " is deleted. </h1><br>" + html)


def Delete(request, listing_id):
    a = Listing.objects.filter(id=listing_id)
    a.delete()

    url = '/realestate/ListView/'
    html = '<a href="' + url + '">' + "Return to list?" + '</a><br>'

    return HttpResponse("<h1>Listing ID " + str(listing_id) + " is deleted. </h1><br>" + html)
