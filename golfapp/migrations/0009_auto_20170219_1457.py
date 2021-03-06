# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 14:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('golfapp', '0008_auto_20170218_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShotPercentages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drivep', models.IntegerField(default=None)),
                ('longironp', models.IntegerField(default=None)),
                ('approachp', models.IntegerField(default=None)),
                ('chipp', models.IntegerField(default=None)),
                ('puttp', models.IntegerField(default=None)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='golfscore',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
