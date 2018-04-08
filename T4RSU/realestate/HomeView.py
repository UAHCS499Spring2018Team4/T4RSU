#!/usr/bin/env python3
# encoding=utf-8

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from .models import Agency
from .models import Listing

from django.contrib.auth import authenticate
#from django.core.context_processors import csrf
from django.shortcuts import render
from django.views.generic import TemplateView
####################################
from .forms import HomeForm
###################################

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form: form'})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)
