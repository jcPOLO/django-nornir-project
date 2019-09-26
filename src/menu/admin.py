from django.contrib import admin

from .models import (
    Device, Template, Platform, Jinja2Template
)

admin.site.register(Device)
admin.site.register(Template)
admin.site.register(Platform)
admin.site.register(Jinja2Template)
