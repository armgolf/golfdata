# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golfapp', '0003_auto_20170114_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='golfscore',
            name='approach3',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='approach4',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='approach5',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='approach6',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='approach7',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='approach8',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='approach9',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='chip3',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='chip4',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='chip5',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='chip6',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='chip7',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='chip8',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='chip9',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='drive3',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='drive4',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='drive5',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='drive6',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='drive7',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='drive8',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='drive9',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='holeno3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='holeno4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='holeno5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='holeno6',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='holeno7',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='holeno8',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='holeno9',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='longiron3',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='longiron4',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='longiron5',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='longiron6',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='longiron7',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='longiron8',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='longiron9',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='par3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='par4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='par5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='par6',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='par7',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='par8',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='par9',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='putt3',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='putt4',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='putt5',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='putt6',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='putt7',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='putt8',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='putt9',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='score3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='score4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='score5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='score6',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='score7',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='score8',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='golfscore',
            name='score9',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='golfscore',
            name='holeno1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='golfscore',
            name='par1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='golfscore',
            name='score1',
            field=models.IntegerField(default=0),
        ),
    ]
