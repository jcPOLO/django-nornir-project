# Generated by Django 2.2.5 on 2019-09-26 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20190926_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='jinja2',
            field=models.TextField(default=''),
        ),
    ]
