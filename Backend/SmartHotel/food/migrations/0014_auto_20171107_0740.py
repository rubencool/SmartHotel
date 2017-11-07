# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-07 07:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0013_auto_20171106_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=10)),
                ('img', models.FileField(upload_to='src/assets/img/')),
                ('imgPath', models.FilePathField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='table',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Section'),
        ),
    ]