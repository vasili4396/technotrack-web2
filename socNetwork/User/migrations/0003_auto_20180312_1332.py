# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-12 13:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20180305_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
