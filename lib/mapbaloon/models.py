from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import User, UserManager
from lib.auth.models import CustomUser

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

class Balloon(models.Model):
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

	syscoord = models.CharField(max_length=255,default='None', blank=True)
	sysaltit = models.CharField(max_length=255,default='None', blank=True)	
	
	instrument = models.ForeignKey(Instrument)

class PolygonCoord(models.Model):
	pgowner = models.ForeignKey(Polygon)
	coord1 = models.FloatField()
	coord2 = models.FloatField()

