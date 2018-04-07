#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import ListView

from . import Listing

class SearchView(ListView):
    template_name = 'SearchView.html'
    model = Listing

    _filter_name_to_lookup = {
        "area_min": "squareFootage__gte",
        "area_max": "squareFootage__lte",
        "price_min": "price__gte",
        "price_max": "price__lte",
        "zip": "zipCode",
    }

    def get_queryset(self):
        get_dict = self.request.GET.dict()
        q = Listing.objects.all()
        # For every filter we understand...
        for filter_name, lookup in SearchView._filter_name_to_lookup.items():
            # ... if it's set...
            if filter_name in get_dict:
                # ... filter based on it.
                q = q.filter(**{lookup: get_dict[filter_name]})
        return q
