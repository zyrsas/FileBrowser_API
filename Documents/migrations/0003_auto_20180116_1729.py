# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-16 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Documents', '0002_auto_20180105_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='access',
            field=models.BooleanField(default=False, verbose_name='Разрешить доступ'),
        ),
    ]
