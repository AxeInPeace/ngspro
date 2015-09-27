# coding=utf-8
from django.contrib.auth.models import User
from django.db import models

class CustomUser(models.Model):
    rating = models.IntegerField(default=0)
    cash = models.PositiveIntegerField(u'Счет кошелька', default=0, blank=False)
    userid = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='avatar/')
