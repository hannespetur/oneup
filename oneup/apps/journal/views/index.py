# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.conf import settings
# from django.views import generic
# from oneup.apps.journal.models import Question, Choice
# from django.utils import timezone

"""
View for index page.
"""


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
    team_name = "Team 1up"
    years_old = 15
    list_of_games = [
        "Counter Strike",
        "Dark Souls",
        "Dota 2",
        "Hearthstone",
        "Starcraft",
        "That mobile app game that ripped off Dota 2 heroes"
    ]
    return render(
        request,
        'public/index.html',
        {
            "team": team_name,
            "years": years_old,
            "journal": "active",
            "games_array": list_of_games,
            "BASE_HREF": settings.BASE_HREF
        }
    )
