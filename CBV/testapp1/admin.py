# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from testapp1.models import Company
# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'ceo']

admin.site.register(Company, CompanyAdmin)