from django.db import models
from lib.core.models import DownloadableMixin


class Photo(DownloadableMixin):
    alt = models.CharField(max_length=255)
