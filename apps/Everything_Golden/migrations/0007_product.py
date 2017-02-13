# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 23:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Everything_Golden', '0006_auto_20170212_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=70, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('orders', models.ManyToManyField(to='Everything_Golden.User')),
            ],
        ),
    ]