# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-07 07:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0014_auto_20171107_0740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='img',
        ),
    ]
