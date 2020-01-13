from __future__ import absolute_import, unicode_literals

from hacker_news.celery import app

from django.core import management


@app.task
def call_get_news():
    management.call_command('get_news')