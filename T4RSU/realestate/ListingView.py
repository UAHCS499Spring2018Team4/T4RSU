#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import DetailView

from .Listing import Listing
from .photo import Photo

class ListingView(DetailView):
    template_name = 'Listing.html'
    model = Listing
    context_object_name = 'Listing'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lis = Listing.objects.get(MLSNumber=self.kwargs['pk'])
        context['photo_list'] = Photo.objects.filter(listing=lis)
        return context
