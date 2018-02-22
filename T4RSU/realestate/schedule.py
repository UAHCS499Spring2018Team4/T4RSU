#!/usr/bin/env python3
# encoding=utf-8

from django.db import models

from .listing import Listing
from .agent import Agent

class Showing(models.Model):
    listing = models.ForeignKey('Listing', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    duration = models.DurationField()
    showing_agent = models.ForeignKey('Agent', on_delete=models.PROTECT)
