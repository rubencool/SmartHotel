# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-06 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0012_auto_20171106_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='cust_id',
            field=models.IntegerField(default=0),
        ),
    ]
