#!/usr/bin/env python3
# encoding=utf-8

from django.views.generic import UpdateView


class ListingEditView(UpdateView):
    template_name = 'ListingEdit.html'
