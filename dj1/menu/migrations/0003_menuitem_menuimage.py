# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_ingredient_menuitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='menuimage',
            field=models.ImageField(default='default.png', upload_to='menuimage/'),
        ),
    ]