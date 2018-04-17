#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

class ShowingEditView(LoginRequiredMixin, UpdateView):
    template_name = 'CreateShowing.html'
