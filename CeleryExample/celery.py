from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CeleryExample.settings')

app = Celery('CeleryExample')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'sum_two_numbers',
        'schedule': 30.0,
        'args': (16, 16)
    },

    'add-every-5-seconds': {
        'task': 'multiply_two_numbers',
        'schedule': 05.0,
        'args': (5, 5)
    },

    'print-every-second':{
        'task': 'rest',
        'schedule': 01.0,
        'args': (10, 2)
    },

    'send-every-6-seconds':{
        'task': 'examplapp.tasks.email',
        'schedule': 2,
        'args': ("salazarpazomar@gmail.com",)
    },
    'send-every-6-secondsdwq':{
        'task': 'examplapp.tasks.email',
        'schedule': 2,
        'args': ("escuela.salazarpazomar@gmail.com",)
    },
    'send-every-6-seconddwqdqws':{
        'task': 'examplapp.tasks.email',
        'schedule': 2,
        'args': ("appledevice.salazarpazomar@gmail.com",)
    },
    'send-every-6-seconqwdqwds':{
        'task': 'examplapp.tasks.email',
        'schedule': 2,
        'args': ("team@platzi.com",)
    },
    'send-every-6-seconqwddsadsaqwds':{
        'task': 'examplapp.tasks.email',
        'schedule': 2,
        'args': ("salazarpazomar@gmail.com",)
    },
}
