# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 04:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_post_bool'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='my_date',
            field=models.DateField(auto_now=True),
        ),
    ]
