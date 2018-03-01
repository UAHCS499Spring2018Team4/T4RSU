#!/usr/bin/env python3
# encoding=utf-8

from django.db import models

from .agency import Agency

class Agent(models.Model):
    """
    Represents a real estate agent.
    """
    employing_agency = models.ForeignKey('Agency', on_delete=models.CASCADE)
