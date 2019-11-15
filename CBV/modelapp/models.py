# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    address = models.CharField(max_length=264)
    class Meta:
        abstract = True

class Student(ContactInfo):
    rollno = models.IntegerField()
    marks = models.IntegerField()

class Teacher(ContactInfo):
    subject = models.CharField(max_length=64)
    salary = models.FloatField()

