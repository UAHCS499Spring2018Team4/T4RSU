from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView
from realestate.ListingCreateView import ListingCreateView
from realestate.views import HomeView


urlpatterns = [
    #path('', views.Overview, name='Overview'),


    #re_path(r'^ListView/$', views.ListView, name='ListView'),

    #re_path(r'^(?P<listing_id>[0-9]+)/del/$', views.Delete, name='Delete'),

    #re_path(r'^(?P<listing_id>[0-9]+)/change/$', views.ListChange, name='ListChange'),

    ##re_path(r'^CreateListing/$', ListingCreateView.as_view(), name='CreateListing'),

    ##re_path(r'^CreateListing/$', TemplateView.as_view(template_name="CreateListing.html")),

    re_path(r'^Home/$', HomeView.as_view(), name='home'),
    #######################################
]