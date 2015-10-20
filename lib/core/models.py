from django.db import models

class DownloadableMixin(models.Model):
    url = models.URLField()

    class Meta:
        abstract = True
