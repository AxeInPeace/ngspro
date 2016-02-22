# encoding=utf-8
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import TemplateView

from lib.core.views import Enggeo


class MainView(Enggeo, TemplateView):
    template_name = 'main/index.html'


def slash(request):
    if request.user.is_authenticated():
        return redirect('map')
    else:
        return render(request, "main/index.html")
