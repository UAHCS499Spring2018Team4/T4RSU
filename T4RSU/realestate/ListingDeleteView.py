#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import DeleteView


class ListingDeleteView(DeleteView):
    template_name = 'ListingDelete.html'
