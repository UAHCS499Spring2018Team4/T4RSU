#!/usr/bin/env python3
# encoding=utf-8

from django.db import models
from django.urls import reverse

from .models import RealEstateAgentUser as Agent

class Listing(models.Model):
    """
    Represents a listing.
    """
    listing_agent = models.ForeignKey(Agent, on_delete=models.PROTECT)
    MLSNumber = models.IntegerField(unique=True, primary_key=True, db_column='id')
    picture = models.ImageField(null=True)
    price = models.DecimalField(max_digits=13, decimal_places=2)    # 1 bn $ sale?
    address = models.TextField()
    zipCode = models.IntegerField()
    squareFootage = models.FloatField()
    description = models.TextField()
    roomDescription = models.TextField()
    subdivision = models.TextField(null=True)
    schoolDistrict = models.TextField()
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
        return reverse('ListingView', kwargs={'pk': self.MLSNumber})

    def __str__(self):
        return 'Number: ' + str(self.MLSNumber)

    def daily_hit_count(self):

        send_mail('Daily Hit Count!', get_templet('templates/realestate/HitCountEmail.html').render(
            Context({
                'MLSNumber': self.MLSNumber,
                'dailyHitCount': self.dailyHitCount,
                'totalHitCount': self.totalHitCount
                     })
        ), 'AutoPoshPlace@gmail.com', [self.listing_agent.email],
                  fail_silently=False)

        self.dailyHitCount = 0
