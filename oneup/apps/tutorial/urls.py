from django.conf.urls import url

from oneup.apps.tutorial.views import tutorial

urlpatterns = [
    # ex: /polls/
    url(r'^$', tutorial.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', tutorial.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', tutorial.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', tutorial.vote, name='vote'),
]