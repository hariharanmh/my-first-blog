# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 06:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0004_shop_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='user_id',
            new_name='shop_user_id',
        ),
    ]
