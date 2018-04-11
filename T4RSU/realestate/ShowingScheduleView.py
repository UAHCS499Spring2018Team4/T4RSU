#!/usr/bin/env python3
# encoding=utf-8

from datetime import date

from django.views.generic import ListView

from .models import Listing, Showing

class ShowingScheduleView(ListView):
    template_name = 'ShowingSchedule.html'
    model = Showing

    def get_queryset(self):
        lis = Listing.objects.get(MLSNumber=self.kwargs['MLSNumber'])
        shows = Showing.objects.filter(listing=lis)
        shows = shows.filter(start_time__gte=date.today())
        return shows
