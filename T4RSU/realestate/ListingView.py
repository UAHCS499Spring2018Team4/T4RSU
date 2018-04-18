#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import DetailView

from .Listing import Listing

class ListingView(DetailView):
    template_name = 'Listing.html'
    model = Listing
    context_object_name = 'Listing'
