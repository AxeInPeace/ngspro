from django.views.generic import TemplateView

from lib.core.views import Enggeo


class ListJobs(Enggeo, TemplateView):
    template_name = 'job/index.html'