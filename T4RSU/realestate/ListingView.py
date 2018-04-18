#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import DetailView

from .Listing import Listing

class ListingView(DetailView):
    template_name = 'Listing.html'
    model = Listing
    context_object_name = 'Listing'

    def get_object(self):
        item = super().get_object()
        item.dailyHitCount = item.dailyHitCount + 1
        item.totalHitCount = item.totalHitCount + 1
        return item