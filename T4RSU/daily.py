#!/usr/bin/env python3
# encoding=utf-8

from realestate.Listing import Listing

def run_daily_emails():
    for entry in Listing.objects.all():
        entry.daily_hit_count()

run_daily_emails()
