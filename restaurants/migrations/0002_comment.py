# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=255)),
                ('visitor', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('date_time', models.DateField()),
                ('restaurant', models.ForeignKey(to='restaurants.Restaurant')),
            ],
        ),
    ]
