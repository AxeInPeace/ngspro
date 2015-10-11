# encoding=utf-8
from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import User, UserManager
from lib.auth.models import CustomUser
from lib.photo.models import Photo



class Format(models.Model):
    name = models.CharField(max_length=15)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Instrument(models.Model):
    name = models.CharField(max_length=511)

    def __unicode__(self):
        return self.name    
    
    def __str__(self):
        return self.name


class GeoObject(models.Model):
    lat = models.IntegerField()
    lng = models.IntegerField()
    class Meta:
        abstract = True



class Balloon(models.Model):
    def __unicode__(self):
        return str(self.coord1) + ' ' + str(self.coord2)
    
    def __str__(self):
        return str(self.coord1) + ' ' + str(self.coord2)

    coord1 = models.FloatField()
    coord2 = models.FloatField()
    date = models.DateField()
    isugrshoot = models.BooleanField(default=False, blank=True) #having underground communication shooting
    isaltmark = models.BooleanField(default=False, blank=True) #having altitude mark
    isrelelems = models.BooleanField(default=False, blank=True) #having relief elements

    publisher = models.ForeignKey(CustomUser)
    myFormat = models.ForeignKey(Format)

    syscoord = models.CharField(max_length=255)
    sysaltit = models.CharField(max_length=255)	
    
    instrument = models.ForeignKey(Instrument)


class Polygon(models.Model):
    date = models.DateField()
    isugrshoot = models.BooleanField(default=False, blank=True) #having underground communication shooting
    isaltmark = models.BooleanField(default=False, blank=True) #having altitude mark
    isrelelems = models.BooleanField(default=False, blank=True) #having relief elements

    publisher = models.ForeignKey(CustomUser)
    myFormat = models.ForeignKey(Format)

    syscoord = models.CharField(max_length=255, default='None', blank=True)
    sysaltit = models.CharField(max_length=255, default='None', blank=True)	
    
    instrument = models.ForeignKey(Instrument)


class PolygonCoord(models.Model):
    pgowner = models.ForeignKey(Polygon)
    coord1 = models.FloatField()
    coord2 = models.FloatField()


class TriangulationStation(GeoObject):
    TYPE_CHOICES = (
        ('trian', 'Пункт триангуляции'),
        ('trial', 'Пункт трилатерации'),
        ('polyg', 'Пункт полигонометрии'),
        ('reper', 'Грунтовый репер'),
        ('znak',  'Стенной знак'),
    )

    title = models.CharField(max_length=255)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES)
    precision = models.IntegerField()
    national = models.BooleanField()
    height = models.IntegerField()
    backsight = models.BooleanField()
    outer = models.BooleanField()
    center = models.BooleanField()
    center_height = models.BooleanField()
    center_photo = models.ForeignKey(Photo)
