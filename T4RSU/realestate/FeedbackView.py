#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import CreateView


class FeedbackView(CreateView):
    template_name = 'CreateFeedback.html'
