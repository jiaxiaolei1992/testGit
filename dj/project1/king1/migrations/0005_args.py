# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 06:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('king1', '0004_mate1_mate2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Args',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('not_name', models.CharField(max_length=20)),
            ],
        ),
    ]
