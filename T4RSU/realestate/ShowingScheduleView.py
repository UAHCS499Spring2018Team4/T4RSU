#!/usr/bin/env python3
# encoding=utf-8

from datetime import date

from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Listing, Showing

class ShowingScheduleView(LoginRequiredMixin, ListView):
    template_name = 'ShowingSchedule.html'
    model = Showing
    context_object_name = 'showing_list'

    def get_queryset(self):
        lis = Listing.objects.get(MLSNumber=self.kwargs['pk'])
        shows = Showing.objects.filter(listing=lis)
        shows = shows.filter(start_time__gte=date.today())
        return shows

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listing'] = Listing.objects.get(MLSNumber=self.kwargs['pk'])
        return context
