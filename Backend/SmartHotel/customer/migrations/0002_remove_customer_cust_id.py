# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-06 06:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='cust_id',
        ),
    ]
