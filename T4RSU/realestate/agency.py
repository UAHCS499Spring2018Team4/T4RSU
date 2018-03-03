#!/usr/bin/env python3
# encoding=utf-8

from django.db import models

class Agency(models.Model):
    """
    Represents a real estate agency.
    """
    agency_name = models.CharField(max_length=1000)
