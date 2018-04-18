#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms

from .Listing import Listing
from .photo import Photo

class ListingEditView(LoginRequiredMixin, UpdateView):
    template_name = 'ModifyListing.html'
    model = Listing
    fields = [#'listing_agent',
        'MLSNumber',
        'picture',
        'price',
        'address',
        'zipCode',
        'squareFootage',
        'description',
        'roomDescription',
        'subdivision',
        'schoolDistrict',
        'shopping',
        'armCode',
        'disarmCode',
        'password',
        'alarmNotes',
        'isOccupied',
        'lockBoxCode',
    ]

    Picture1 = forms.ImageField(required=False)

    def form_invalid(self, form):
        raise ValueError(str(form.errors))

    def form_valid(self, form):
        redir = super().form_valid(form)
        raise ValueError(form.cleaned_data)
        if form.cleaned_data['Picture1']:
            Photo(listing=self.kwargs['pk'], picture=form.cleaned_data['Picture1']).save()
        return redir
