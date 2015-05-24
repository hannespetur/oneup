import datetime

from django.db import models
from django.utils import timezone


class Journal(models.Model):
    title = models.CharField(max_length=200)
    posted_date = models.DateTimeField('date posted')

    def was_posted_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.posted_date <= now

    def __unicode__(self):
        return self.title
