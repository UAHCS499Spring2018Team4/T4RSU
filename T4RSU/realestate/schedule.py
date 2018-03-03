#!/usr/bin/env python3
# encoding=utf-8

from django.db import models

from .listing import Listing
from .models import RealEstateAgentUser as Agent

def doShowingsOverlap(a: 'Showing', b: 'Showing') -> bool:
    """
    Test if scheduled showings overlap in time.
    Does not test for listings being the same.

    :param a: one showing

    :param b: another showing

    :return: if the showings overlap
    """
    st1 = a.start_time
    st2 = b.start_time
    et1 = st1 + a.duration
    et2 = st2 + b.duration
    if(st1 < et2):
        # Make sure one ends before the other begins
        return bool(et1 < st2)
    else:
        # b ends before a begins
        return True

class Showing(models.Model):
    """
    Represents a showing.
    """
    listing = models.ForeignKey('Listing', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    duration = models.DurationField()
    showing_agent = models.ForeignKey('Agent', on_delete=models.PROTECT)
