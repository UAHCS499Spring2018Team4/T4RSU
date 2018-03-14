#!/usr/bin/env python3
# encoding=utf-8

from django.db import models

class Agency(models.Model):
    """
    Represents a real estate agency.
    """
    agency_name = models.CharField(max_length=1000)
    agency_address = models.CharField(max_length=1000, null=True)
    agency_phone = models.CharField(max_length=1000, null=True)


    def __str__(self):
        return self.agency_name