# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-18 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='regform1',
            name='password',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
