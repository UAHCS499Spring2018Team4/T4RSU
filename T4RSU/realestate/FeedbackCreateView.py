#!/usr/bin/env python3
# encoding=utf-8


from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm
from django.views.generic import CreateView
from django.urls import reverse
from django.core.mail import send_mail

from .feedback import Feedback

class FeedbackCreateForm(ModelForm):
    def __init__(self, showing, *args, **kwargs):
        # need to take showing
        super().__init__(*args, **kwargs)
        self.showing = showing

    class Meta:
        model = Feedback
        fields = ['showing', 'customerName', 'customerInterest', 'overallExperience', 'customerPriceOpinion', 'showerPriceOpinion', 'additionalNotes']
#
#    def clean(self):
#        cleaned_data = super().clean()
#        start = datetime(cleaned_data.get('start_time'))
#        dur = timedelta(cleaned_data.get('dur'))
#        if not is_showing_td_available(self.listingMLS, start, dur):
#            raise ValidationError(_("Listing already booked for showing at that time."), code='overlap')
#        return cleaned_data
#

class FeedbackCreateView(LoginRequiredMixin, CreateView):
    template_name = 'CreateFeedback.html'
    model = Feedback
    fields = ['showing', 'customerName', 'costomerInterest', 'overallExperience', 'customerPriceOpinion',
              'showerPriceOpinion', 'additionalNotes']


    def form_valid(self, form):
        message = """
        Here is what {{showing.showing_agent.username}} Had to say about the showing.
        Customer Name: {{customerName}}.
        Customer Interest; {{costomerInterest}}/10
        Overall Experience; {{overallExperience}}/10
        Customer's Opinion of the Price; {{customerPriceOpinion}}/10
        Showing Agent's Opinion of the Price: {{showerPriceOpinion}}/10
        Additional Notes: {{additionalNotes}}
        """

        send_mail('Feedback Recieved!', message.as_string(), 'AutoPoshPlace', '{{showing.listing.listing_agent.email}}', fail_silently=False)

        return super().form_valid(form)

    def get_success_url(self):
        # redirect to showings for listing
        return reverse('showings', kwargs={'MLSNumber': self.get_object().listing.MLSNumber})
