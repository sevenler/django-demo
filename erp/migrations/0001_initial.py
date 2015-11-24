# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('edited_time', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('icon', models.CharField(max_length=500)),
                ('desc', models.CharField(max_length=1000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('edited_time', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0)),
                ('brand', models.CharField(max_length=36)),
                ('generated_id', models.CharField(max_length=36)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OperationRecord',
            fields=[
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('edited_time', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('user_id', models.CharField(max_length=36)),
                ('model', models.CharField(max_length=200)),
                ('operation', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('before', models.IntegerField()),
                ('after', models.IntegerField()),
                ('description', models.CharField(max_length=2000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Procurement',
            fields=[
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('edited_time', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('expenses', models.FloatField(default=0)),
                ('launch_user_id', models.CharField(max_length=36)),
                ('procurement_id', models.CharField(max_length=36)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProcurementEntry',
            fields=[
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('edited_time', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('product_id', models.CharField(max_length=36)),
                ('price', models.FloatField(default=0)),
                ('number', models.IntegerField(default=0)),
                ('entry_id', models.CharField(max_length=36)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
