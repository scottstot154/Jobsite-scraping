from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab # scheduler
# default django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE','dscrap.settings')
app = Celery('sc1', broker='amqp://', backend='rpc://',
	include=['sc1.tasks'])
app.conf.timezone = 'UTC'
app.config_from_object("django.conf:settings")
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
	print(f'Request: {self.request!r}')