from django.contrib import admin

from .models import Balloon, Polygon, Format, Instrument, TriangulationStation


admin.site.register(Balloon)
admin.site.register(Polygon)
admin.site.register(Format)
admin.site.register(Instrument)
admin.site.register(TriangulationStation)
