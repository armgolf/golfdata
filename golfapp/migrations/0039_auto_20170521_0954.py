# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-21 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golfapp', '0038_signup_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='phonenumber',
            field=models.CharField(max_length=20),
        ),
    ]
