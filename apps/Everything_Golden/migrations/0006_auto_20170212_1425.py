# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Everything_Golden', '0005_auto_20170212_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(default='0', null=True),
        ),
    ]