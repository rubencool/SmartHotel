# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-04 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_table_tabel_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='registered',
            field=models.BooleanField(default=False),
        ),
    ]
