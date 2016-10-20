from __future__ import unicode_literals

from django.db import models


class UserType(models.Model):
    name=models.CharField(max_length=50)

class UserInfo(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    IPadress=models.CharField(max_length=50)
    Age=models.IntegerField(default=1)
    memo=models.TextField(default='xxxx')
    Gender=models.BooleanField(default=False)
    CreateDat=models.DateTimeField(default='2014-10-21 12:12')

    typeID=models.ForeignKey('UserType')

class Group(models.Model):
    Name=models.CharField(max_length=50)

class User(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)

    gtoup_relation=models.ManyToManyField('Group')

class Mate1(models.Model):
    Name=models.CharField(max_length=50)

class Mate2(models.Model):
    Name=models.CharField(max_length=50)
    relation=models.OneToOneField('Mate1')

class Args(models.Model):
    name=models.CharField(max_length=20,null=True)
    not_name=models.CharField(max_length=20,null=False)

class Show(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    sex=models.CharField(max_length=20,null=False)

class Asset(models.Model):
    hostname=models.CharField(max_length=25)
    create_date=models.DateTimeField(auto_now=True)
    upate_date=models.DateTimeField(auto_now=True)

class Temp(models.Model):
    GENDER_CHOICE=(
        (u'M',u'Male'),
        (u'F',u'Female'),

    )
    gender=models.CharField(max_length=2,choices=GENDER_CHOICE)





# Create your models here.
