from celery.task.schedules import crontab
from celery.decorators import periodic_task
from .Listing import Listing
from celery.utils.log import get_task_logger
from datetime import datetime

logger = get_task_logger(__name__)


@periodic_task(run_every=(crontab(hour="16", minute="03", day_of_week="*")))
def run_daily_emails():
    for entry in Listing.objects.all():
        entry.daily_hit_count()
