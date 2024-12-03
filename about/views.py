# about/views.py
from django.shortcuts import render


def about_me(request):
    return render(request, "about/about_me.html")
