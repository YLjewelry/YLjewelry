# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-05 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelrydisplay', '0006_auto_20180605_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
