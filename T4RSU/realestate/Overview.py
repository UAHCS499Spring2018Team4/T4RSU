#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import TemplateView

class OverviewView(TemplateView):
    template_name = 'LandingPage.html'
