# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-19 01:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('open_work', '0004_auto_20170118_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='tag',
        ),
        migrations.AddField(
            model_name='jobs',
            name='body',
            field=models.TextField(default=''),
        ),
    ]