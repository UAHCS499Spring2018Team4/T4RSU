#!/usr/bin/env python3
# encoding=utf-8


from django.db import models

from .schedule import Showing

class Feedback(models.Model):
    """
    Feedback for a showing.
    """
    showing = models.ForeignKey('Showing', on_delete=models.PROTECT)
    customerInterest = models.IntegerField()
    overallExperience = models.IntegerField()
    customerPriceOpinion = models.IntegerField()
    showerPriceOpinion = models.IntegerField()
    additionalNotes = models.TextField()
