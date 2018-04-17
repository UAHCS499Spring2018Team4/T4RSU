#!/usr/bin/env python3
# encoding=utf-8


from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm
from django.views.generic import CreateView
from django.urls import reverse
from django.core.mail import send_mail

from .feedback import Feedback
from .Listing import Listing

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
    fields = ['showing', 'customerName', 'customerInterest', 'overallExperience', 'customerPriceOpinion',
              'showerPriceOpinion', 'additionalNotes']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listing'] = Listing.objects.get(MLSNumber=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        send_mail('Feedback Recieved!', get_templete('templates/realestate/FeedbackEmail.html').render(
            Context({
                'username': self.showing.showing_agent.username,
                'customerName': self.customerName,
                'costomerInterest': self.costomerInterest,
                'overallExperience': self.overallExperience,
                'customerPriceOpinion': self.customerPriceOpinion,
                'showerPriceOpinion': self.showerPriceOpinion,
                'additionalNotes': self.additionalNotes
                     })), 'AutoPoshPlace@gmail.com', '{{showing.listing.listing_agent.email}}', fail_silently=False)


        return super().form_valid(form)

    def get_success_url(self):
        # redirect to showings for listing
        return reverse('showings', kwargs={'MLSNumber': self.get_object().listing.MLSNumber})
