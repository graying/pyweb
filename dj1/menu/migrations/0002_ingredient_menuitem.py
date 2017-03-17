# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 08:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Menuitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menuitem_text', models.CharField(max_length=200)),
                ('howspicy', models.IntegerField(default=0)),
                ('vegetarian', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Category')),
                ('ingredient', models.ManyToManyField(to='menu.Ingredient')),
            ],
        ),
    ]