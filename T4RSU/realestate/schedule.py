#!/usr/bin/env python3
# encoding=utf-8

from django.db import models

from .listing import Listing

class Showing(models.Model):
    listing = models.ForeignKey('Listing', on_delete=models.CASCADE)
