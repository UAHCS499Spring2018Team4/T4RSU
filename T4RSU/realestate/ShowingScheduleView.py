#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import TemplateView


class ShowingScheduleView(TemplateView):
    template_name = 'ListOfShowings.html'
