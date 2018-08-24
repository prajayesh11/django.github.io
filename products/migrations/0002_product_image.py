# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-13 10:30
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=products.models.upload_image_path),
        ),
    ]
