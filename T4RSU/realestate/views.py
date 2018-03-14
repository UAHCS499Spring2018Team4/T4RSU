from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from .models import Agency
from django.contrib.auth import authenticate
#from django.core.context_processors import csrf
from django.shortcuts import render

def index(request):

    return HttpResponse("<h2>Hello World</h2>")



def demo(request):
    all_agencies = Agency.objects.all()
    template = loader.get_template('realestate/demo.html')
    context = {
        'all_agencies': all_agencies,
    }
    return HttpResponse(template.render(context, request))

