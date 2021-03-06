# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_menuitem_menuimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='ingredient_text_cn',
            field=models.CharField(default='Chinese name', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='menuitex_text_cn',
            field=models.CharField(default='Chinese name', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
