# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-31 09:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('golfapp', '0018_golfcourses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golfscore',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='golfapp.GolfCourses'),
        ),
    ]
