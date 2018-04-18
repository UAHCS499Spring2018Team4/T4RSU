#!/usr/bin/env python3
# encoding=utf-8

from django.forms import ModelForm
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms

from .Listing import Listing
from .photo import Photo

class ListingCreateForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['listing_agent',
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
            'Picture1',
            'Picture2',
            'Picture3',
            'Picture4',
            'Picture5',
        ]
    Picture1 = forms.ImageField(required=False)
    Picture2 = forms.ImageField(required=False)
    Picture3 = forms.ImageField(required=False)
    Picture4 = forms.ImageField(required=False)
    Picture5 = forms.ImageField(required=False)

    picfieldnames = [
        'Picture1',
        'Picture2',
        'Picture3',
        'Picture4',
        'Picture5',
    ]

class ListingCreateView(LoginRequiredMixin, CreateView):
    template_name = 'CreateListing.html'
    model = Listing
    form_class = ListingCreateForm
    Picture1 = forms.ImageField(required=False)

    def form_invalid(self, form):
        raise ValueError(str(form.errors))

    def form_valid(self, form):
        form.instance.save()
        for field in ListingCreateForm.picfieldnames:
            if field in form.cleaned_data:
                Photo(listing=form.instance, picture=form.cleaned_data.get(field)).save()
        return super().form_valid(form)
