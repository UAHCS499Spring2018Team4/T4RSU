#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic.edit import FormView
from django import forms
from django.forms import Form
from django.urls import reverse

from .Listing import Listing

class SearchForm(Form):
    template_name = 'AdvancedSearch.html'

    area_min = forms.FloatField()
    area_max = forms.FloatField()
    price_min = forms.DecimalField(max_digits=13, decimal_places=2)
    price_max = forms.DecimalField(max_digits=13, decimal_places=2)
    zip = forms.IntegerField()

class SearchView(FormView):
    template_name = 'AdvancedSearch.html'
    form_class = SearchForm

    def form_valid(self, form):
        self.form = form
        return super().form_valid(form)

    def form_invalid(self, form):
        raise ValueError('test')

    def get_success_url(self):
        redirect = "{}?area_min={}&area_max={}&price_min={}&price_max={}&zip={}".format(reverse('allview'),
            self.form.area_min, self.form.area_max, self.form.price_min, self.form.price_max, self.form.zip)
        return redirect
