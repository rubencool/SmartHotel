# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-06 07:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0008_remove_table_checkout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='item',
        ),
        migrations.RemoveField(
            model_name='order',
            name='table_no',
        ),
        migrations.RemoveField(
            model_name='order',
            name='which_waiter',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]