# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0007_product_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[(b'S', b'Small'), (b'M', b'Medium'), (b'L', b'Large')], default=b'M', max_length=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]