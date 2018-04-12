#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import CreateView
from .Listing import Listing
from django.shortcuts import render


class ListingCreateView(CreateView):
    template_name = 'CreateListing.html'
    model = Listing
    fields = ['listing_agent',
        'MLSNumber',
        #'picture',
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
