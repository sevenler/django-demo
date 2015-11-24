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
    ]
