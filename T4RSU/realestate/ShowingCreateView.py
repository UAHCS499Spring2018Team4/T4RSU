#!/usr/bin/env python3
# encoding=utf-8

from datetime import datetime, timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm, ValidationError
from django.views.generic import CreateView
from django.urls import reverse

from .Listing import Listing
from .schedule import Showing, is_showing_td_available

class ShowingCreateForm(ModelForm):
    def __init__(self, listingMLS, *args, **kwargs):
        # need to take listingMLS
        super().__init__(*args, **kwargs)
        self.listingMLS = listingMLS

    class Meta:
        model = Showing
        fields = ['start_time', 'duration']

    def clean(self):
        cleaned_data = super().clean()
        start = datetime(cleaned_data.get('start_time'))
        dur = timedelta(cleaned_data.get('dur'))
        if not is_showing_td_available(self.listingMLS, start, dur):
            raise ValidationError(_("Listing already booked for showing at that time."), code='overlap')
        return cleaned_data

class ShowingCreateView(LoginRequiredMixin, CreateView):
    template_name = 'CreateShowing.html'
    model = Showing
    fields = ['start_time', 'duration']
    form_class = ShowingCreateForm

    def get_form_kwargs(self):
        # have to pass listing
        kwargs = super().get_form_kwargs()
        kwargs['listingMLS'] = self.kwargs['MLSNumber']
        return kwargs

    def form_valid(self, form):
        form.instance.listing = Listing.objects.get(MLSNumber=self.kwargs['MLSNumber'])
        form.instance.showing_agent = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # redirect to showings for listing
        return reverse('showings', kwargs={'MLSNumber': self.get_object().listing.MLSNumber})
