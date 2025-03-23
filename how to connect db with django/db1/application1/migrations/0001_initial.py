# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2025-03-14 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField()),
                ('sname', models.CharField(max_length=21)),
                ('subject', models.CharField(max_length=21)),
                ('marks', models.FloatField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
