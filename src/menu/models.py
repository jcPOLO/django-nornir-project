from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import datetime
from django.utils import timezone


class Device(models.Model):

    host = models.CharField(max_length=100, null=False)
    ip_address = models.GenericIPAddressField(null=False)
    platform = models.CharField(max_length=20, null=True)
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
    phone = PhoneNumberField(null=True, blank=True, unique=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - code: {self.site_code}'


class Menu(models.Model):
    menu_choices = (
        ('option 1', 'option 1 choice'),
        ('option 2', 'option 2 choice'),
        ('option 3', 'option 3 choice'),
        ('option 4', 'option 4 choice')
    )
    template = models.BooleanField()
