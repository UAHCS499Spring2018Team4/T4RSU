#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import CreateView, TemplateView
from realestate.listing import Listing
from django.shortcuts import render
from realestate.forms import HomeForm


class ListingCreateView(CreateView):
    template_name = 'CreateListing.html'

    model = Listing
    fields = ['address', 'description', 'isOccupied']