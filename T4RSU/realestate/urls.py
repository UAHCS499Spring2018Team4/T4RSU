from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.OverviewView.as_view(), name='Overview'),
    path('search/', views.SearchView.as_view(), name='SearchView'),
    path('Listing/<int:MLSNumber>/', views.ListingView.as_view(), name='ListingView'),
    path('Listing/<int:MLSNumber>/Delete/', views.ListingDeleteView.as_view(), name='Delete'),
    path('Listing/<int:MLSNumber>/Edit/', views.ListingEditView.as_view(), name='ListChange'),
]
