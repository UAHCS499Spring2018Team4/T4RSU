#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import CreateView
from .Listing import Listing
from django.shortcuts import render


class ListingCreateView(CreateView):
    template_name = 'CreateListing.html'
    model = Listing
    fields = ['MLS', 'primaryPicture', 'price', 'address', 'zipCode', 'squareFoot', 'generalDescription', 'roomDescription', 'subDivision', 'school', 'shopping', 'armCode', 'disarmCode', 'password', 'alarmNotes', 'lockBoxCode', 'isOccupied']

    