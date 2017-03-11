# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=64, null=True)),
                ('ref', models.CharField(blank=True, default='', max_length=64, null=True)),
            ],
        ),
    ]
