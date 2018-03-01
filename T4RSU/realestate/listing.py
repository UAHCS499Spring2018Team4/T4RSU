#!/usr/bin/env python3
# encoding=utf-8

from django.db import models

from .agent import Agent

class Listing(models.Model):
    """
    Represents a listing.
    """
    listing_agent = models.ForeignKey('Agnet', on_delete=models.PROTECT)
