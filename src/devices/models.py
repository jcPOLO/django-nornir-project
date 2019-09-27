from django.db import models
import datetime
from django.utils import timezone
from phone_field import PhoneField


class Platform(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class ModelType(models.Model):
    name = models.CharField(max_length=30)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Site(models.Model):

    name = models.CharField(max_length=100, null=True)
    address = models.TextField()
    site_code = models.CharField(max_length=10, null=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - code: {self.site_code}'


class Device(models.Model):

    hostname = models.CharField(max_length=100, null=False)
    ip_address = models.GenericIPAddressField(null=False)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.SET(1))
    serial = models.CharField(max_length=100, null=False)
    is_telnet = models.BooleanField(null=False, default=False)
    is_ssh = models.BooleanField(null=False, default=False)
    role = models.CharField(max_length=10, null=True)
    model_type = models.ManyToManyField(ModelType)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.hostname}-{self.ip_address}'
