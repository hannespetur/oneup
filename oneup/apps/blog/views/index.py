#-*- coding: utf-8 -*-
from django.shortcuts import render
"""
View for index page.
"""

def page(request):
    # fetch three newest blog posts
    three_newest_posts = [
        {
            'title': 'this is title 1',
            'post_date': 'yesterday',
            'body': 'this is body 1'
        },
        {
            'title': 'this is title 2',
            'post_date': 'today',
            'body': 'this is body 2'
        }
    ]
    return render(
        request,
        'public/index.html',
        {
            "three_newest_posts": three_newest_posts,
        }
    )
