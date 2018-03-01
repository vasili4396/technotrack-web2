# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('likes_count', models.PositiveIntegerField(default=0)),
                ('comments_count', models.PositiveIntegerField(default=0)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(unique=True, max_length=127)),
                ('first_name', models.CharField(null=True, max_length=255)),
                ('last_name', models.CharField(null=True, max_length=255)),
                ('sex', models.CharField(choices=[('M', 'male'), ('F', 'female')], blank=True, null=True, max_length=1)),
                ('is_admin', models.BooleanField(default=False)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('city', models.CharField(blank=True, null=True, max_length=255)),
                ('country', models.CharField(blank=True, null=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='avatar',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
