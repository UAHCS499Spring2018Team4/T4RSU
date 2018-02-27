#!/usr/bin/env python3
# encoding=utf-8

from django.db import models

from .agency import Agency

class Agent(models.Model):
    employing_agency = models.ForeignKey('Agency', on_delete=models.CASCADE)
