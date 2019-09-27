from django.contrib import admin
from .models import Template, Jinja2Template

admin.site.register(Template)
admin.site.register(Jinja2Template)
