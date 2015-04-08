from django.conf.urls import url

from . import polls

urlpatterns = [
    # ex: /polls/
    url(r'^$', polls.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', polls.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', polls.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', polls.vote, name='vote'),
]