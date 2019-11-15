# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=60)
    ceo = models.CharField(max_length=60)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk":self.pk})



