from django.contrib import admin

from devices.models import (
    Device, Platform, Site, ModelType
)

admin.site.register(Device)
admin.site.register(Platform)
admin.site.register(Site)
admin.site.register(ModelType)
