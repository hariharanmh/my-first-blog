# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0012_auto_20171123_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_sale_quantity',
            field=models.IntegerField(max_length=16, verbose_name='Sale Quantity'),
        ),
    ]
