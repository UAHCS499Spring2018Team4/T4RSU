#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import CreateView
from .Listing import Listing
from django.shortcuts import render


class ListingCreateView(CreateView):
    template_name = 'CreateListing.html'
    model = Listing
    fields = ['MLSNumber']

    def post(self, request):
        form = Listing(request.POST)

        return render(request, self.template_name, {'form': form})
