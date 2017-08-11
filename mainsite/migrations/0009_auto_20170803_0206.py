# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 18:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0008_auto_20170803_0139'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-pub_date',)},
        ),
        migrations.AddField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]