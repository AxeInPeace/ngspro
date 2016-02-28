from django.contrib import admin

from .models import Balloon, Polygon, Format, Instrument, TriangulationStation
from django.contrib import admin


class BalloonAdmin(admin.ModelAdmin):
    list_display = ('title', 'lng', 'lat', 'date', 'is_published')
    list_filter = ('is_published',)

admin.site.register(Balloon, BalloonAdmin)
admin.site.register(Polygon)
admin.site.register(Format)
admin.site.register(Instrument)
admin.site.register(TriangulationStation)
