# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Everything_Golden', '0011_auto_20170213_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_event',
            field=models.DateField(),
        ),
    ]
