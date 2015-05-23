from django.conf.urls import url

from oneup.apps.journal.views import details
from oneup.apps.journal.views import index

urlpatterns = [
    # ex: /journal/
    url(r'^$', index.page, name='index'),
    # ex: /journal/5/
    url(r'^(?P<pk>[0-9]+)/$', details.page, name='details'),
]