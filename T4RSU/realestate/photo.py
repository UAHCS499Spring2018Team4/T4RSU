#!/usr/bin/env python3
# encoding=utf-8


from django.db import models
from .listing import Listing

class Photo(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    picture = models.ImageField()
