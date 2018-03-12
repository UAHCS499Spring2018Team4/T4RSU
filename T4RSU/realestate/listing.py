#!/usr/bin/env python3
# encoding=utf-8

from django.db import models

from .models import RealEstateAgentUser as Agent

from .agency import Agency

class Listing(models.Model):
    """
    Represents a listing.
    """
    listing_agent = models.ForeignKey('Agent', on_delete=models.PROTECT)
    MLSNumber = models.IntegerField()
    picture = models.ImageField()
    price = models.DecimalField(max_digits=13, decimal_places=2)    # 1 bn $ sale?
    address = models.TextField()
    squareFootage = models.FloatField()
    listing_agency = models.ForeignKey('Agency', on_delete=models.PROTECT) # TODO: Remove me
    description = models.TextField()
    roomDescription = models.TextField()
    subdivision = models.TextField(null=True)
    schoolDistrict = models.TextField()
    shopping = models.TextField()
    totalHitCount = models.IntegerField()
    dailyHitCount = models.IntegerField()
    armCode = models.TextField(null=True)
    disarmCode = models.TextField(null=True)
    password = models.TextField(null=True)
    alarmNotes = models.TextField()
    isOccupied = models.BooleanField()
    lockBoxCode = models.TextField()    # TODO: nullable?
