"""
INF601 - Advanced Programming in Python
Mini Project 4 - Django small web app
Sam Boutros
Prof. Zeller
FHSU - Fall 2022
11/6/2022
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    return render(request, 'blog/home.html')
