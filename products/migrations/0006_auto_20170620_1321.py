# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-20 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_products_product_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_count',
            field=models.IntegerField(default=0),
        ),
    ]
