# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-10 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_assignment_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task', models.CharField(max_length=100)),
                ('Topic', models.CharField(max_length=100)),
                ('Question1', models.CharField(max_length=500)),
                ('Question2', models.CharField(max_length=500)),
                ('Question3', models.CharField(max_length=500)),
                ('Question4', models.CharField(max_length=500)),
                ('Question5', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='NodeJSTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task', models.CharField(max_length=100)),
                ('Topic', models.CharField(max_length=100)),
                ('Question1', models.CharField(max_length=500)),
                ('Question2', models.CharField(max_length=500)),
                ('Question3', models.CharField(max_length=500)),
                ('Question4', models.CharField(max_length=500)),
                ('Question5', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='PLSQLTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task', models.CharField(max_length=100)),
                ('Topic', models.CharField(max_length=100)),
                ('Question1', models.CharField(max_length=500)),
                ('Question2', models.CharField(max_length=500)),
                ('Question3', models.CharField(max_length=500)),
                ('Question4', models.CharField(max_length=500)),
                ('Question5', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='PythonTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task', models.CharField(max_length=100)),
                ('Topic', models.CharField(max_length=100)),
                ('Question1', models.CharField(max_length=500)),
                ('Question2', models.CharField(max_length=500)),
                ('Question3', models.CharField(max_length=500)),
                ('Question4', models.CharField(max_length=500)),
                ('Question5', models.CharField(max_length=500)),
            ],
        ),
    ]
