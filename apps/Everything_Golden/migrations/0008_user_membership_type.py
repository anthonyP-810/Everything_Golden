# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 01:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Everything_Golden', '0007_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='membership_type',
            field=models.IntegerField(null=True),
        ),
    ]