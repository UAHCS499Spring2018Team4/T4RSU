#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .Listing import  Listing

class ListingDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'ListingDelete.html'
    model = Listing

    success_url = reverse_lazy('Overview')
