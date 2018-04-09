from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from .models import Agency
from .models import Listing
from django.contrib.auth import authenticate
#from django.core.context_processors import csrf
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
####################################
from realestate.forms import HomeForm
###################################


from . import (
    FeedbackView,
    ListingCreateView,
    ListingDeleteView,
    ListingEditView,
    Overview,
    SearchView,
    ShowingEditView,
    ShowingScheduleView
)

#####################################
class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            form = HomeForm()
            a = Listing(address=text)
            a.save()

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)
