from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.OverviewView.as_view(), name='Overview'),

    path('search/', views.SearchView, name='SearchView'),

    re_path(r'^(?P<listing_id>[0-9]+)/del/$', views.ListingDeleteView, name='Delete'),

    re_path(r'^(?P<listing_id>[0-9]+)/change/$', views.ListingEditView, name='ListChange'),

]