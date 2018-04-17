#!/usr/bin/env python3
# encoding=utf-8

from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.OverviewView.as_view(), name='Overview'),
    path('search/', views.SearchView.as_view(), name='SearchView'),
    path('Listing/<int:pk>/', views.ListingView.as_view(), name='ListingView'),
    path('Listing/<int:pk>/Delete/', views.ListingDeleteView.as_view(), name='Delete'),
    path('Listing/<int:pk>/Edit/', views.ListingEditView.as_view(), name='ListChange'),
    path('Listing/<int:pk>/Showings/', views.ShowingScheduleView.as_view(), name='showings'),
    path('Listing/<int:pk>/Showings/Create', views.ShowingCreateView.as_view(), name='showingcreate'),
    path('Listing/<int:pk>/Showings/<int:sk>/Feedback', views.FeedbackCreateView.as_view(), name='feedback'),
    path('Create/', views.ListingCreateView.as_view(), name='CreateListing'),
    path('Home/', views.HomeView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='LogIn.html'), name='login'),
    path('AllListings/', views.AllView.as_view(), name='allview'),
]
