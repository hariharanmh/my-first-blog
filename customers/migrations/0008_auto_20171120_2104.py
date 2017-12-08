# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 15:34
from __future__ import unicode_literals

import customers.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_auto_20171118_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_phone_number',
            field=models.CharField(max_length=16, validators=[customers.validators.validate_phone_number]),
        ),
    ]