#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .Listing import Listing
from .photo import Photo
from .ListingForm import ListingForm

class ListingEditView(LoginRequiredMixin, UpdateView):
    template_name = 'ModifyListing.html'
    model = Listing
    form_class = ListingForm

    def form_invalid(self, form):
        raise ValueError(str(form.errors))

    def form_valid(self, form):
        redir = super().form_valid(form)
        for field in ListingForm.picfieldnames:
            if field in form.cleaned_data and form.cleaned_data.get(field):
                Photo(listing=form.instance, picture=form.cleaned_data.get(field)).save()
        return redir
