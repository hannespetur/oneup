import datetime

from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField('Post title', max_length=200)
    slug = models.SlugField('Url string', max_length=100, unique=True)
    body = models.TextField('Post body')
    post_date = models.DateTimeField('Date published', auto_now_add=True)
    edited_date = models.DateTimeField('Date changed')
    visible = models.BooleanField(
        'Visible',
        default=False,
        help_text= 'Check this to make the post visible on webpage'
    )
    category = models.ForeignKey('blog.Category')

    def was_published_recently(self):
        return self.post_date >= timezone.now() - datetime.timedelta(days=1)

    def was_changed_recently(self):
        return self.edited_date >= timezone.now() - datetime.timedelta(days=1)

    def __unicode__(self):
        return '%s' % self.title

    # see doc for get_absolute_url:
    # https://docs.djangoproject.com/en/1.8/ref/models/instances/#get-absolute-url
    @permalink
    def get_absolute_url(self):
        return '/posts/%s/%s' % (self.id, self.slug)

class Category(models.Model):
    title = models.CharField('Category title', max_length=100, unique=True)
    slug = models.SlugField('Url string', max_length=100, unique=True)
    description = models.TextField('Category description')

    def __unicode__(self):
        return '%s' % self.title

    # see doc for get_absolute_url:
    # https://docs.djangoproject.com/en/1.8/ref/models/instances/#get-absolute-url
    @permalink
    def get_absolute_url(self):
        return '/posts-by-category/%s' % self.slug
