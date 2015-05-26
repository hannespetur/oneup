# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.conf import settings
# from django.views import generic
# from oneup.apps.journal.models import Question, Choice
# from django.utils import timezone

from oneup.apps.journal.models import Journal

'''
View for journal index.
'''


# class IndexView(generic.ListView):
#     template_name = 'public/index.html'
#     context_object_name = 'latest_question_list'
#
#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.filter(
#             pub_date__lte=timezone.now()
#             ).order_by('-pub_date')[:5]

def page(request):
    last_five_visible_journals = Journal.objects.filter(visible=1).order_by('-id')[:5]
    #from pdb import set_trace; set_trace()
    return render(
        request,
        'public/index.html',
        {
            'BASE_HREF': settings.BASE_HREF,
            'journals': last_five_visible_journals
        }
    )
