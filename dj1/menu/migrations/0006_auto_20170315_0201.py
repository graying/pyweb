# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 02:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20170314_0810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='ingredient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='menu.Ingredient'),
            preserve_default=False,
        ),
    ]
