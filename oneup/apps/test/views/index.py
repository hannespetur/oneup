#-*- coding: utf-8 -*-
from django.shortcuts import render
"""
View for index page.
"""

def page(request):
    team_name = "Team 1up"
    years_old = 15
    list_of_games = ["Counter Strike", "Dark Souls", "Dota 2", "Hearthstone", "Starcraft", "That mobile app game that ripped off Dota 2 heroes"]
    return render(request, 'en/public/index.html', {"team": team_name, "years": years_old, "tab": "index", "games_array": list_of_games})
