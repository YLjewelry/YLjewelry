# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-29 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelrydisplay', '0012_series_series_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='series_sequence',
            field=models.IntegerField(default=0),
        ),
    ]
