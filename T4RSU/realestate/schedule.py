#!/usr/bin/env python3
# encoding=utf-8

from datetime import datetime, timedelta

from django.db import models

from .Listing import Listing
from .models import RealEstateAgentUser as Agent

def do_td_overlap(t1: datetime, d1: timedelta, t2: datetime, d2: timedelta) -> bool:
    et1 = t1 + d1
    et2 = t2 + d2
    if(t1 < et2):
        # Make sure one ends before the other begins
        return bool(et1 < t2)
    else:
        # b ends before a begins
        return True

def do_showings_overlap(a: 'Showing', b: 'Showing') -> bool:
    """
    Test if scheduled showings overlap in time.
    Does not test for listings being the same.

    :param a: one showing

    :param b: another showing

    :return: if the showings overlap
    """
    return do_td_overlap(a.start_time, a.duration, b.start_time, b.duration)

def is_showing_td_available(listing_: 'Listing', time: datetime, duration: timedelta) -> bool:
    showings_applicable = Showing.objects.filter(listing=listing_)
    return not any(map(lambda ls: do_td_overlap(ls.start_time, ls.duration, time, duration), showings_applicable))

class Showing(models.Model):
    """
    Represents a showing.
    """
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    duration = models.DurationField()
    showing_agent = models.ForeignKey(Agent, on_delete=models.PROTECT)
