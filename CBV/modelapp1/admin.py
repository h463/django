# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from modelapp1.models import ContactInfo1,Student1,Teacher1, Parent, Child1, Child2
# Register your models here.

#Multi table inheritance
admin.site.register(ContactInfo1)
admin.site.register(Student1)
admin.site.register(Teacher1)

#Multilevel inheritance
admin.site.register(Parent)
admin.site.register(Child1)
admin.site.register(Child2)