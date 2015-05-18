# -*- coding: utf-8 -*-
from django.shortcuts import render

"""
View for about page.
"""


def page(request):
    return render(
        request,
        'en/public/about.html',
        {
            "about": "active"
        }
    )