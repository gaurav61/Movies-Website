# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-12 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('release_date', models.DateField()),
                ('image', models.ImageField(upload_to=b'')),
                ('movie_id', models.IntegerField()),
                ('duration', models.DurationField()),
            ],
        ),
    ]
