#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import CreateView, TemplateView
from realestate.listing import Listing
from django.shortcuts import render
from realestate.forms import HomeForm


class ListingCreateView(CreateView):
    template_name = 'home.html'

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            field1 = form.cleaned_data['address']
            field2 = form.cleaned_data['description']
            field3 = form.cleaned_data['isOccupied']
            a = Listing(address=field1, description=field2, isOccupied=field3)
            a.save()

        args = {'form': form, 'text': field1}
        return render(request, self.template_name, args)