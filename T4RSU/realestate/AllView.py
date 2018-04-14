#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import ListView

from .Listing import Listing

class AllView(ListView):
    template_name = 'AllListings.html'
    model = Listing
    context_object_name = 'listing_list'
