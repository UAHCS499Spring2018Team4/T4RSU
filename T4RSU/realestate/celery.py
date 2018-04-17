from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from .Listing import Listing

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('T4RSU')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@periodic_task(run_every=(crontab(hour="6", minute="0")))
def run_daily_emails():
    Listing.daily_hit_count()
