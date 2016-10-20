# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 02:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('king1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='typeID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='king1.UserType'),
            preserve_default=False,
        ),
    ]