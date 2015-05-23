#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.conf import settings

"""
View for index page.
"""

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
        'en/public/index.html',
        {
            "team": team_name,
            "years": years_old,
            "index": "active",
            "games_array": list_of_games,
            "BASE_HREF": settings.BASE_HREF
        }
    )
