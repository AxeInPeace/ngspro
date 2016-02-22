# encoding=utf-8
from django.db import models

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
    def __unicode__(self):
        return self.__str__()
    
    def __str__(self):
        return self.title + '(' + str(self.lat) + ', ' + str(self.lng) + ')'

    title = models.CharField(max_length=255, verbose_name="Название")
    lat = models.FloatField(verbose_name="Широта")
    lng = models.FloatField(verbose_name="Долгота")
    publisher = models.ForeignKey(CustomUser, verbose_name="Автор")
    date = models.DateField(verbose_name="Дата")
    class Meta:
        abstract = True


class Balloon(GeoObject):
    isugrshoot = models.BooleanField(blank=True) #having underground communication shooting
    isaltmark = models.BooleanField(blank=True) #having altitude mark
    isrelelems = models.BooleanField(blank=True) #having relief elements

    myFormat = models.ForeignKey(Format)

    syscoord = models.CharField(max_length=255)
    sysaltit = models.CharField(max_length=255)	
    
    instrument = models.ForeignKey(Instrument)
    material_photo = models.ForeignKey(Photo) 
    material = models.URLField()


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

    type = models.CharField(max_length=7, choices=TYPE_CHOICES, verbose_name="Тип")
    precision = models.IntegerField(verbose_name="Класс точности")
    national = models.BooleanField(verbose_name="Государственный?")
    height = models.IntegerField(verbose_name="Высота над уровнем моря")
    backsight = models.BooleanField(verbose_name="Ориентирный знак сохранился?")
    outer = models.BooleanField(verbose_name="Наружный знак сохранился?")
    center = models.BooleanField(verbose_name="Центр сохранился?")
    center_height = models.IntegerField(verbose_name="Положение относительно земли, м")
    center_photo = models.ForeignKey(Photo, verbose_name="Фото центра", null=True)

    @property
    def images(self):
        return [self.center_photo] if self.center_photo else []

    class Meta:
        verbose_name = "Тригопункт"
        verbose_name_plural = "Тригопункты"

