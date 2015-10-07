# encoding=utf-8
from django.shortcuts import render

def landing(request):
    context = {}
    return render(request, "landing/landing.html", context)
