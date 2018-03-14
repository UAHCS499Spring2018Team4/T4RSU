#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import UpdateView

class ShowingEditView(UpdateView):
    template_name = 'ShowingEdit.html'
