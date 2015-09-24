from django.contrib import admin

from .models import baloon, polygon, formats, instruments


admin.site.register(baloon)
admin.site.register(polygon)
admin.site.register(formats)
admin.site.register(instruments)

