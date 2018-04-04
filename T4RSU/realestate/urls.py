from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.Overview, name='Overview'),


    re_path(r'^ListView/$', views.ListView, name='ListView'),

    re_path(r'^(?P<listing_id>[0-9]+)/del/$', views.Delete, name='Delete'),

    re_path(r'^(?P<listing_id>[0-9]+)/change/$', views.ListChange, name='ListChange'),

]