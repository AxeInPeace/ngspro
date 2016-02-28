from django.contrib.auth.models import User
from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Payment(models.Model):
    user = models.ForeignKey(User)
    sum = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Cost(models.Model):
    content_type = models.ForeignKey(ContentType)
    cost = models.PositiveIntegerField()
