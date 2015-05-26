import datetime

from django.db import models
from django.db.models import permalink
from django.utils import timezone
from django.conf import settings
from django.core.urlresolvers import reverse


class Journal(models.Model):
    title = models.CharField('Post title', max_length=200)
    slug = models.SlugField('Url string', max_length=100, unique=True)
    posted_date = models.DateTimeField('Date posted', default=datetime.datetime.now)
    body = models.TextField('Post body', default='')
    category = models.ForeignKey('journal.Category', blank=True, null=True)
    visible = models.BooleanField(
        'Visible',
        default = False,
        help_text = 'Check this to make the post visible on webpage'
    )

    def was_posted_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.posted_date <= now

    def __unicode__(self):
        return self.title

    # see doc for get_absolute_url:
    # https://docs.djangoproject.com/en/1.8/ref/models/instances/#get-absolute-url
    #@permalink
    #def get_absolute_url(self):
    #    #return '%sjournal/%s/%s' % (settings.BASE_HREF, self.id, self.slug)
    #    return reverse('journal:details', kwargs={'journal_id': str(self.id), 'slug': self.slug})

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField('Name', max_length=100, unique=True)
    slug = models.SlugField('Slug', max_length=100, unique=True)
    description = models.TextField('Description')

    def __unicode__(self):
        return '%s' % self.name

    # see doc for get_absolute_url:
    # https://docs.djangoproject.com/en/1.8/ref/models/instances/#get-absolute-url
    #def get_absolute_url(self):
    #    return '/journals-by-category/%s' % self.slug
