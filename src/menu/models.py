from django.db import models
import datetime
from django.utils import timezone
from phone_field import PhoneField


class Platform(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Device(models.Model):

    host = models.CharField(max_length=100, null=False)
    ip_address = models.GenericIPAddressField(null=False)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    site_code = models.CharField(max_length=10, null=True)
    serial = models.CharField(max_length=100, null=False)
    is_telnet = models.CharField(max_length=5, null=True)
    role = models.CharField(max_length=10, null=True)
    model = models.CharField(max_length=30, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.host} {self.hostname}'


class Site(models.Model):

    name = models.CharField(max_length=100, null=True)
    address = models.TextField()
    site_code = models.CharField(max_length=10, null=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - code: {self.site_code}'


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
