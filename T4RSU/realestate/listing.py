#!/usr/bin/env python3
# encoding=utf-8

from django.db import models

from .models import RealEstateAgentUser as Agent

from .agency import Agency

class Listing(models.Model):
    listing_agent = models.ForeignKey('Agent', on_delete=models.PROTECT)
    MLSNumber = models.IntegerField
    picture = models.ImageField()
    price = models.FloatField
    #Address?
    squareFootage = models.FloatField
    listing_agency = models.ForeignKey('Agency', on_delete=models.PROTECT)
    description = models.TextField
    roomDescription = models.TextField
    subdivision = models.TextField #can be null
    schoolDistrict = models.TextField
    shopping = models.TextField
    #schedule = models.ForeignKey('Showing', on_delete=models.PROTECT) Removed due to group discussion
    totalHitCount = models.IntegerField
    dailyHitCount = models.IntegerField
    armCode = models.IntegerField
    disarmCode = models.IntegerField
    password = models.TextField
    alarmNotes = models.TextField
    isOcupied = models.BooleanField
    lockBoxCode = models.IntegerField

