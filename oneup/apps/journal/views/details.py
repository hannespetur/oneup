# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.conf import settings
# from django.views import generic
# from oneup.apps.journal.models import Question, Choice
# from django.utils import timezone


"""
View for about page.
"""


# class DetailView(generic.DetailView):
#    model = Question
#    template_name = 'public/details.html'
#
#    def get_queryset(self):
#        """
#        Excludes any questions that aren't published yet.
#        """
#        return Question.objects.filter(pub_date__lte=timezone.now())


def page(request, journal_id, slug=None):
    if slug in ['', None]:
        slug = 'Slug was empty'

    return render(
        request,
        'public/details.html',
        {
            "journal": "active",
            "BASE_HREF": settings.BASE_HREF,
            "journal_id": journal_id,
            'slug': slug
        }
    )