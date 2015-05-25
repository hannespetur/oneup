from django.conf.urls import url

from oneup.apps.journal.views import details
from oneup.apps.journal.views import index

urlpatterns = [
    # ex: /journal/
    url(r'^$', index.page, name='index'),
    # ex: /journal/5/
    url(r'^(?P<journal_id>[0-9]+)(?:\/(?P<slug>.*)?)?$', details.page, name='details'),
]