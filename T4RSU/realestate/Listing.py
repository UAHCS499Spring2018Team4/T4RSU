#!/usr/bin/env python3
# encoding=utf-8

from django.db import models
from django.urls import reverse

from .models import RealEstateAgentUser as Agent

class Listing(models.Model):
    """
    Represents a listing.
    """
    #listing_agent = models.ForeignKey(Agent, on_delete=models.PROTECT)
    MLS = models.IntegerField(unique=True)
    primaryPicture = models.ImageField()
    price = models.DecimalField(max_digits=13, decimal_places=2)    # 1 bn $ sale?
    address = models.TextField()
    zipCode = models.IntegerField()
    squareFoot = models.FloatField()
    generalDescription = models.TextField()
    roomDescription = models.TextField()
    subDivision = models.TextField(null=True)
    school = models.TextField()
    shopping = models.TextField()
    totalHitCount = models.IntegerField(default=0)
    dailyHitCount = models.IntegerField(default=0)
    armCode = models.TextField(null=True)
    disarmCode = models.TextField(null=True)
    password = models.TextField(null=True)
    alarmNotes = models.TextField()
    isOccupied = models.BooleanField()
    lockBoxCode = models.TextField()    # TODO: nullable?

    def get_absolute_url(self):
        return reverse('ListingView', kwargs={'MLSNumber': self.MLS})

    def __str__(self):
        #return 'Number: ' + str(self.MLSNumber)
        return str(self.address)

    def get_absolute_url(self):
        pass

