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
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=128)),
                ('customer_phone_number', models.CharField(max_length=16, unique=True)),
                ('customer_email_id', models.EmailField(blank=True, max_length=256, null=True)),
                ('customer_sale_quantity', models.CharField(blank=True, max_length=16, null=True)),
                ('customer_sale_quantity_desc', models.TextField(blank=True, null=True)),
                ('customer_sale_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_of_entry', models.DateTimeField(auto_now_add=True)),
                ('date_of_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
