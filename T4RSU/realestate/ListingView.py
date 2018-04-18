#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import DetailView

from .Listing import Listing

class ListingView(DetailView):
    template_name = 'Listing.html'
    model = Listing
    context_object_name = 'Listing'

    def get_object(self, queryset):
        item = super().get_object(queryset)
        self.dailyHitCount = self.dailyHitCount + 1
        self.totalHitCount = self.totalHitCount + 1
        return item