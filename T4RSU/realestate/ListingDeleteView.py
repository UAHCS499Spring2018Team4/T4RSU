#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import DeleteView

from .Listing import  Listing

class ListingDeleteView(DeleteView):
    template_name = 'ListingDelete.html'
    model = Listing
