from django.db import models
import datetime
from django.utils import timezone
from devices.models import Platform


class Template(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    platform = models.ManyToManyField(Platform)

    def __str__(self):
        return self.name


class Jinja2Template(models.Model):
    config = models.TextField(default='')
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.template}_{self.platform}'

    def get_jinja2(self):
        return self.config
