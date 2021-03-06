# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-28 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20190225_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Traineename', models.CharField(max_length=100)),
                ('Totalassignments', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Assignment1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TraineeName', models.CharField(max_length=100, verbose_name=b'Name')),
                ('AssignmentName', models.CharField(max_length=100, verbose_name=b'Assignment Name')),
                ('CourseName', models.CharField(choices=[(b'python', b'Python'), (b'plsql', b'PlSql'), (b'Django', b'Django'), (b'Node.js', b'Node.js')], default=b'Python', max_length=50, verbose_name=b'Course')),
            ],
        ),
    ]
