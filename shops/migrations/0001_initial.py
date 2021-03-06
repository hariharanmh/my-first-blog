# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=128)),
                ('shop_phone_number', models.CharField(max_length=16, unique=True)),
                ('shop_city', models.CharField(max_length=128)),
                ('shop_address', models.TextField(blank=True, null=True)),
                ('shop_category', models.CharField(max_length=128)),
                ('shop_type', models.CharField(max_length=128)),
                ('date_of_entry', models.DateTimeField(auto_now_add=True)),
                ('date_of_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
