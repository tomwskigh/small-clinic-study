# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-26 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_visit', '0011_auto_20171226_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medical',
            name='nickname',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]