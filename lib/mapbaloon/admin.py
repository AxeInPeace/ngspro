from django.contrib import admin

from .models import custom_user, baloon, polygon, formats, instruments


admin.site.register(custom_user)
admin.site.register(baloon)
admin.site.register(polygon)
admin.site.register(formats)
admin.site.register(instruments)

