#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import CreateView


class ListingCreateView(CreateView):
    template_name = 'CreateListing.html'
