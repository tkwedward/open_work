# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-20 00:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('open_work', '0008_auto_20170119_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='tag',
            field=models.CharField(default='', max_length=20),
        ),
    ]