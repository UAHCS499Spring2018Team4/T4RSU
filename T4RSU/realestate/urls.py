from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^demo/$', views.demo, name='demo'),

    url(r'^ListView/$', views.ListView, name='ListView'),

    url(r'^(?P<listing_id>[0-9]+)/del/$', views.Delete, name='Delete'),

    url(r'^(?P<listing_id>[0-9]+)/change/$', views.ListChange, name='ListChange'),

]