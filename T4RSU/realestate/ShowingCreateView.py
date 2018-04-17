#!/usr/bin/env python3
# encoding=utf-8

from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm, ValidationError
from django.views.generic import CreateView
from django.urls import reverse
from django import forms
from django.core.mail import send_mail

from .Listing import Listing
from .schedule import Showing, is_showing_td_available

class ShowingCreateForm(ModelForm):
    start_time = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M:%S',    # '2006-10-25 14:30:59'
        '%Y-%m-%d %H:%M',       # '2006-10-25 14:30'
        '%Y-%m-%dT%H:%M',  # '2006-10-25 14:30'
        '%m/%d/%Y %H:%M:%S',    # '10/25/2006 14:30:59'
        '%m/%d/%Y %H:%M',       # '10/25/2006 14:30'
        '%m/%d/%Y',             # '10/25/2006'
        '%m/%d/%y %H:%M:%S',    # '10/25/06 14:30:59'
        '%m/%d/%y %H:%M',       # '10/25/06 14:30'
        '%m/%d/%y']             # '10/25/06'
    )
    duration = forms.DurationField()

    def __init__(self, listingMLS, *args, **kwargs):
        # need to take listingMLS
        super().__init__(*args, **kwargs)
        self.listingMLS = listingMLS

    class Meta:
        model = Showing
        fields = ['start_time', 'duration']

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start_time')
        dur = cleaned_data.get('duration')
        if not is_showing_td_available(self.listingMLS, start, dur):
            raise ValidationError(("Listing already booked for showing at that time."), code='overlap')
        return cleaned_data

class ShowingCreateView(LoginRequiredMixin, CreateView):
    template_name = 'CreateShowing.html'
    model = Showing
    form_class = ShowingCreateForm

    def get_form_kwargs(self):
        # have to pass listing
        kwargs = super().get_form_kwargs()
        kwargs['listingMLS'] = self.kwargs['pk']
        return kwargs

    def form_valid(self, form):
        form.instance.listing = Listing.objects.get(MLSNumber=self.kwargs['pk'])
        form.instance.showing_agent = self.request.user

        send_mail('Showing Created!', get_templet('templates/realestate/ShowingEmail.html').render(
            Context({
                'username': self.showing_agent.username,
                'MLSNumber': self.listing.MLSNumber,
                'start_time': self.start_time
                     })), 'AutoPoshPlace@gmail.com', [form.instance.listing.listing_agent.email],
                  fail_silently=False)

        return super().form_valid(form)

    def get_success_url(self):
        # redirect to showings for listing
        return reverse('showings', kwargs={'MLSNumber': self.get_object().listing.MLSNumber})
