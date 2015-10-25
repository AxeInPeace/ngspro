# coding=utf-8
from django.contrib.auth.models import User
from django.db import models

class CustomUser(models.Model):
    def __unicode__(self):
        return self.userid.username

    def __str__(self):
        return self.userid.username
    rating = models.IntegerField(default=0)
    cash = models.PositiveIntegerField(u'Счет кошелька', default=0, blank=False)
    userid = models.OneToOneField(User)
    avatar = models.URLField(blank=True)
