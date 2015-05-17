from django.conf.urls import url

from oneup.apps.tutorial.views import tutorial

urlpatterns = [
    # ex: /polls/
    # url(r'^$', tutorial.index, name='index'),
    url(r'^$', tutorial.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    url(r'^(?P<pk>[0-9]+)/$', tutorial.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', tutorial.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', tutorial.vote, name='vote'),
]