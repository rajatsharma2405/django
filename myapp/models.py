# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here
from django.db import models

# Create your models here.


class User(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=1, default='F')
    has_verified_mobile = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
