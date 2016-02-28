# coding=utf-8
from django.db import models
from lib.core.models import DownloadableMixin


class Photo(DownloadableMixin):
    alt = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'
