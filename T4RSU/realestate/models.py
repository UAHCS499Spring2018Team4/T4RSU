#!/usr/bin/env python3
# encoding=utf-8

# Create your models here.

from .agency import Agency
from .agent import RealEstateAgentUser
from .feedback import Feedback
from .listing import Listing
from .photo import Photo
from .schedule import Showing
from django.urls import reverse
from django.db import models


class ListingCreate(models.Model):
    MLSNumber = models.IntegerField()

    def get_absolute_url(self):
        return reverse('listing-detail', kwargs={'pk': self.pk})

