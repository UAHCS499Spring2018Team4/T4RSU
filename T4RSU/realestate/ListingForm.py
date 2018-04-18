#!/usr/bin/env python3
# encoding=utf-8

from django import forms
from django.forms import ModelForm

from .Listing import Listing

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
            'listing_agent',
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
