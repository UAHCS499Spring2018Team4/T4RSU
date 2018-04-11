#!/usr/bin/env python3
# encoding=utf-8

from django.urls import path
from . import views

urlpatterns = [
    path('', views.OverviewView.as_view(), name='Overview'),
    path('search/', views.SearchView.as_view(), name='SearchView'),
    path('Listing/<int:MLSNumber>/', views.ListingView.as_view(), name='ListingView'),
    path('Listing/<int:MLSNumber>/Delete/', views.ListingDeleteView.as_view(), name='Delete'),
    path('Listing/<int:MLSNumber>/Edit/', views.ListingEditView.as_view(), name='ListChange'),
    path('Listing/<int:MLSNumber>/Showings/', views.ShowingScheduleView.as_view(), name='showings'),
    path('Listing/<int:MLSNumber>/Showings/Create', views.ShowingCreateView.as_view(), name='showingcreate'),
    path('Create/', views.ListingCreateView.as_view(), name='CreateListing'),
    path('Home/', views.HomeView.as_view(), name='home'),
]
