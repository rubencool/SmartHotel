# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-07 12:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0018_section_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='imgPath',
        ),
    ]