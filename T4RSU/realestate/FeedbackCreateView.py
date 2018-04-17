#!/usr/bin/env python3
# encoding=utf-8

from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm
from django.views.generic import CreateView
from django.urls import reverse
from django.core.mail import send_mail
from django.template.loader import get_template

from .models import Showing
from .feedback import Feedback
from .Listing import Listing

class FeedbackCreateForm(ModelForm):
    def __init__(self, showing, *args, **kwargs):
        # need to take showing
        super().__init__(*args, **kwargs)
        self.showing = Showing.objects.get(id=showing)

    class Meta:
        model = Feedback
        fields = ['customerName', 'customerInterest', 'overallExperience', 'customerPriceOpinion', 'showerPriceOpinion', 'additionalNotes']

class FeedbackCreateView(LoginRequiredMixin, CreateView):
    template_name = 'CreateFeedback.html'
    model = Feedback
    form_class = FeedbackCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listing'] = Listing.objects.get(MLSNumber=self.kwargs['pk'])
        return context

    def get_form_kwargs(self):
        # have to pass listing
        kwargs = super().get_form_kwargs()
        kwargs['showing'] = self.kwargs['sk']
        return kwargs

    def form_valid(self, form):
        form.instance.showing = Showing.objects.get(id=self.kwargs['sk'])
        send_mail('Feedback Recieved!', get_template('FeedbackEmail.html').render(
            {
                'username': form.instance.showing.showing_agent.username,
                'customerName': form.instance.customerName,
                'customerInterest': form.instance.customerInterest,
                'overallExperience': form.instance.overallExperience,
                'customerPriceOpinion': form.instance.customerPriceOpinion,
                'showerPriceOpinion': form.instance.showerPriceOpinion,
                'additionalNotes': form.instance.additionalNotes
                     }), 'AutoPoshPlace@gmail.com', [form.instance.showing.listing.listing_agent.email], fail_silently=False)


        return super().form_valid(form)

    def form_invalid(self, form):
        raise ValueError(form.errors)

    def get_success_url(self):
        # redirect to showings for listing
        return reverse('showings', kwargs={'pk': self.kwargs['pk']})
