# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 04:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=264, unique=True),
        ),
    ]