# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('king1', '0006_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='sex',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]