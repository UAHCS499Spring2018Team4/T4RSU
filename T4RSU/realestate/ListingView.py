#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import DetailView

from . import listing

class ListingView(DetailView):
    template_name = 'Listing.html'
    queryset = listing.object.all()
    context_object_name = 'Listing'
