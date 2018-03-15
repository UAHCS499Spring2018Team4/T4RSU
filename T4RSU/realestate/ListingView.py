#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import DetailView

class ListingView(DetailView):
    template_name = 'ListingView.html'
