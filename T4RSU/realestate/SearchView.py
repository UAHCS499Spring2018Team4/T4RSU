#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic.edit import FormView
from django import forms
from django.forms import Form
from django.urls import reverse

class SearchForm(Form):
    template_name = 'AdvancedSearch.html'

    area_min = forms.FloatField(required=False)
    area_max = forms.FloatField(required=False)
    price_min = forms.DecimalField(max_digits=13, decimal_places=2, required=False)
    price_max = forms.DecimalField(max_digits=13, decimal_places=2, required=False)
    zip = forms.IntegerField(required=False)

class SearchView(FormView):
    template_name = 'AdvancedSearch.html'
    form_class = SearchForm

    def form_valid(self, form):
        self.form = form
        return super().form_valid(form)

    def form_invalid(self, form):
        raise ValueError('test')

    def def_str(x: str):
        if x is None:
            return ''
        else:
            return x

    def get_success_url(self):
        redirect = "{}?area_min={}&area_max={}&price_min={}&price_max={}&zip={}".format(
            reverse('allview'),
            SearchView.def_str(self.form.cleaned_data['area_min']),
            SearchView.def_str(self.form.cleaned_data['area_max']),
            SearchView.def_str(self.form.cleaned_data['price_min']),
            SearchView.def_str(self.form.cleaned_data['price_max']),
            SearchView.def_str(self.form.cleaned_data['zip']))
        return redirect
