# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render, redirect
from django.conf import settings
# from django.views import generic
# from django.utils import timezone

from oneup.apps.journal.models import Journal

'''
View for specific journal.
'''


def page(request, journal_id, slug):
    journal = get_object_or_404(Journal, pk=journal_id)
    if journal.slug != slug:
        return redirect('%sjournal/%s/%s' % (settings.BASE_HREF, journal.id, journal.slug))

    return render(
        request,
        'public/details.html',
        {
            'BASE_HREF': settings.BASE_HREF,
            'title': journal.title,
            'posted_date': journal.posted_date,
            'body': journal.body
        }
    )