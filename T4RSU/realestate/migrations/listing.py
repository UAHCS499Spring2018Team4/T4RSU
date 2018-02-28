#!/usr/bin/env python3
# encoding=utf-8

from django.db import models

from .schedule import Showing
from .agent import Agent

class Listing(models.Model):
    MLSNumber = models.IntegerField
    #Primary Picture
    price = models.FloatField
    #Address
    squareFootage = models.FloatField
    listingAgent = models.ForeignKey('Agent', on_delete=models.PROTECT)
    #Listing Agency
    description = models.TextField
    roomDescription = models.TextField
    subdivision = models.TextField #can be null
    schoolDistrict = models.TextField
    shopping = models.TextField
    schedule = models.ForeignKey('Showing', on_delete=models.PROTECT) #May need to become a list or one to many relation
    totalHitCount = models.IntegerField
    dailyHitCount = models.IntegerField
    armCode = models.IntegerField
    disarmCode = models.IntegerField
    password = models.TextField
    alarmNotes = models.TextField
    isOcupied = models.BooleanField
    lockBoxCode = models.IntegerField
