# coding=utf-8
from django.contrib.auth.models import User
from django.db import models

class User(models.Model):
    email = models.EmailField(u'Электронная почта', unique=True)
    cache = models.PositiveIntegerField(u'Счет кошелька', default=0, blank=False)
    django_user = models.OneToOneField(User)
