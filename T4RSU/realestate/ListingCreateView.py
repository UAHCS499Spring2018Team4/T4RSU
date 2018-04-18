#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .Listing import Listing
from .photo import Photo
from .ListingForm import ListingForm

class ListingCreateView(LoginRequiredMixin, CreateView):
    template_name = 'CreateListing.html'
    model = Listing
    form_class = ListingForm

    def form_invalid(self, form):
        raise ValueError(str(form.errors))

    def form_valid(self, form):
        form.instance.save()
        for field in ListingForm.picfieldnames:
            if field in form.cleaned_data:
                Photo(listing=form.instance, picture=form.cleaned_data.get(field)).save()
        return super().form_valid(form)
