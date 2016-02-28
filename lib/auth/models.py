# coding=utf-8
import datetime

from django.contrib.auth.models import User
from django.db import models


class CustomUser(models.Model):
    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.user.username

    rating = models.IntegerField(default=0)
    cash = models.PositiveIntegerField(u'Счет кошелька', default=0, blank=False)
    user = models.OneToOneField(User)
    avatar = models.URLField(blank=True)
    is_registered = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class EmailApprove(models.Model):
    user = models.ForeignKey(CustomUser)
    value = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        verbose_name = "Подтверждение на email"
        verbose_name_plural = "Подтверждения на email"
