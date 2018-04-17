#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import ListView

from .Listing import Listing

class AllView(ListView):
    template_name = 'AllListings.html'
    model = Listing
    context_object_name = 'listing_list'

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
        for filter_name, lookup in self.__class__._filter_name_to_lookup.items():
            # ... if it's set...
            if filter_name in get_dict and get_dict[filter_name]:
                # ... filter based on it.
                q = q.filter(**{lookup: get_dict[filter_name]})
        return q
