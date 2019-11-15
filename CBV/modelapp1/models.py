# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ContactInfo1(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    address = models.CharField(max_length=264)

class Student1(ContactInfo1):
    rollno = models.IntegerField()
    marks = models.IntegerField()

class Teacher1(ContactInfo1):
    subject = models.CharField(max_length=64)
    salary = models.FloatField()

class Parent(models.Model):
    f1 = models.CharField(max_length=64)
    f2 = models.CharField(max_length=64)

class Child1(Parent):
    f3 = models.CharField(max_length=64)
    f4 = models.CharField(max_length=64)

class Child2(Child1):
    f5 =  models.CharField(max_length=64)