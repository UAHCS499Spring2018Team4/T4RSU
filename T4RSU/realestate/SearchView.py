#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import ListView

class SearchView(ListView):
    template_name = 'SearchView.html'
