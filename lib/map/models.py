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

    class Meta:
        verbose_name = "Формат материалов"
        verbose_name_plural = "Форматы материалов"


class Instrument(models.Model):
    name = models.CharField(max_length=511)

    def __unicode__(self):
        return self.name    
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Инструмент"
        verbose_name_plural = "Инструмены"


class GeoPoint(models.Model):
    def __unicode__(self):
        return self.__str__()
    
    def __str__(self):
        return self.title + '(' + str(self.lat) + ', ' + str(self.lng) + ')'

    title = models.CharField(max_length=255, verbose_name=u"Название")
    lat = models.FloatField(verbose_name=u"Широта")
    lng = models.FloatField(verbose_name=u"Долгота")
    publisher = models.ForeignKey(CustomUser, verbose_name=u"Автор")
    date = models.DateField(verbose_name=u"Дата добавления")
    is_published = models.BooleanField(verbose_name=u"Материал показан на сайте", default=False)

    class Meta:
        abstract = True


class Balloon(GeoPoint):
    isugrshoot = models.BooleanField(blank=True)  # having underground communication shooting
    isaltmark = models.BooleanField(blank=True)  # having altitude mark
    isrelelems = models.BooleanField(blank=True)  # having relief elements

    myFormat = models.ForeignKey(Format)

    syscoord = models.CharField(max_length=255)
    sysaltit = models.CharField(max_length=255)	
    
    instrument = models.ForeignKey(Instrument)
    material_photo = models.ForeignKey(Photo) 
    material = models.URLField()

    class Meta:
        verbose_name = "Топосъемка"
        verbose_name_plural = "Топосъемки"


class Polygon(models.Model):
    date = models.DateField()
    isugrshoot = models.BooleanField(default=False, blank=True)  # having underground communication shooting
    isaltmark = models.BooleanField(default=False, blank=True)  # having altitude mark
    isrelelems = models.BooleanField(default=False, blank=True)  # having relief elements

    publisher = models.ForeignKey(CustomUser)
    myFormat = models.ForeignKey(Format)

    syscoord = models.CharField(max_length=255, default='None', blank=True)
    sysaltit = models.CharField(max_length=255, default='None', blank=True)	
    
    instrument = models.ForeignKey(Instrument)


class PolygonCoord(models.Model):
    pgowner = models.ForeignKey(Polygon)
    coord1 = models.FloatField()
    coord2 = models.FloatField()


class TriangulationStation(GeoPoint):
    TYPE_CHOICES = (
        ('trian', 'Пункт триангуляции'),
        ('trial', 'Пункт трилатерации'),
        ('polyg', 'Пункт полигонометрии'),
        ('reper', 'Грунтовый репер'),
        ('znak',  'Стенной знак'),
    )

    type = models.CharField(max_length=7, choices=TYPE_CHOICES, verbose_name="Тип", null=True)
    precision = models.IntegerField(verbose_name="Класс точности", null=True)
    national = models.BooleanField(verbose_name="Государственный?", null=True)
    height = models.FloatField(verbose_name="Высота над уровнем моря", null=True)
    backsight = models.BooleanField(verbose_name="Ориентирный знак сохранился?", null=True)
    outer = models.BooleanField(verbose_name="Наружный знак сохранился?", null=True)
    center = models.BooleanField(verbose_name="Центр сохранился?", null=True)
    center_height = models.FloatField(verbose_name="Положение относительно земли, м", null=True)
    center_photo = models.ForeignKey(Photo, verbose_name="Фото центра", null=True)

    @property
    def images(self):
        return [self.center_photo] if self.center_photo else []

    class Meta:
        verbose_name = "Тригопункт"
        verbose_name_plural = "Тригопункты"

