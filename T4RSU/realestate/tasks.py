from celery.task.schedules import crontab
from celery.decorators import periodic_task
from .Listing import Listing
from celery.utils.log import get_task_logger
from datetime import datetime

logger = get_task_logger(__name__)


@periodic_task(run_every=(crontab(hour="6", minute="0")))
def run_daily_emails():
    Listing.daily_hit_count()