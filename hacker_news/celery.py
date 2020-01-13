from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hacker_news.settings')

app = Celery('hacker_news')

app.config_from_object('django.conf:settings', silent=True, namespace='CELERY')

app.autodiscover_tasks()