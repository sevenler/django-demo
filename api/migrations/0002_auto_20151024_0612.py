# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('generated_id', models.CharField(max_length=36)),
                ('icon', models.CharField(max_length=500)),
                ('desc', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('edited_time', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0)),
                ('brand', models.CharField(max_length=36)),
                ('generated_id', models.CharField(max_length=36)),
            ],
        ),
        migrations.DeleteModel(
            name='Goods',
        ),
    ]
