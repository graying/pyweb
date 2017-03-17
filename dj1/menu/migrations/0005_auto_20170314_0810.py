# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20170314_0215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='vegetarian',
            new_name='is_vegetarian',
        ),
        migrations.RenameField(
            model_name='menuitem',
            old_name='howspicy',
            new_name='spicy_level',
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='menuimage',
            field=models.ImageField(default='menuimage/default.png', upload_to='menuimage/'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='menuitex_text_cn',
            field=models.CharField(default='Chinese name', max_length=200),
        ),
    ]
