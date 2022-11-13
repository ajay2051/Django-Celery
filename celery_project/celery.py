from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
# from django_celery_beat.models import PeriodicTask


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_project.settings')

app = Celery('celery_project')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kathmandu')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery Beat Settings
app.conf.beat_schedule = {
    'send-mail-everyday-8':{
    'task':'mail.tasks.send_mail_func',
    'schedule': crontab(hour=8, minute=0, day_of_month=2, month_of_year=6)
    }
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')