# encoding=utf-8
from django.views.generic import TemplateView

from lib.core.views import Enggeo


class LandingView(Enggeo, TemplateView):
    template_name = "landing/landing.html"
