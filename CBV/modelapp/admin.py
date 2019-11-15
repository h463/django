# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from modelapp.models import ContactInfo,Student,Teacher
# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)