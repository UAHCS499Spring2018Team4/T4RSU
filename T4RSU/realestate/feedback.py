#!/usr/bin/env python3
# encoding=utf-8


from django.db import models

from .shcedule import Showing

class Feedback(models.Model):
    showing = models.ForeignKey('Showing', on_delete=models.PROTECT)
    customerInterest = models.IntegerField
    overallExperience = models.IntegerField
    customerPriceOpinion = models.IntegerField
    showerPriceOpinion = models.IntegerField
    additionalNotes = models.TextField