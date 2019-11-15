# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-13 01:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='Student1',
            fields=[
                ('contactinfo1_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='modelapp1.ContactInfo1')),
                ('rollno', models.IntegerField()),
                ('marks', models.IntegerField()),
            ],
            bases=('modelapp1.contactinfo1',),
        ),
        migrations.CreateModel(
            name='Teacher1',
            fields=[
                ('contactinfo1_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='modelapp1.ContactInfo1')),
                ('subject', models.CharField(max_length=64)),
                ('salary', models.FloatField()),
            ],
            bases=('modelapp1.contactinfo1',),
        ),
    ]