# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 14:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0011_auto_20171120_2212'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='customer',
            unique_together=set([]),
        ),
    ]
