#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .Listing import Listing


class ListingEditView(LoginRequiredMixin, UpdateView):
    template_name = 'ModifyListing.html'
    model = Listing
    fields = [#'listing_agent',
        'MLSNumber',
        'picture',
        'price',
        'address',
        'zipCode',
        'squareFootage',
        'description',
        'roomDescription',
        'subdivision',
        'schoolDistrict',
        'shopping',
        'armCode',
        'disarmCode',
        'password',
        'alarmNotes',
        'isOccupied',
        'lockBoxCode',
    ]

    def form_invalid(self, form):
        raise ValueError(str(form.errors))
