#!/usr/bin/env python3
# encoding=utf-8


from django.db import models
from .Listing import Listing

class Photo(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='primary_photos/')
