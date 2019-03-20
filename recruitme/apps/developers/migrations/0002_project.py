# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=20, choices=[(b'en', b'English'), (b'nl', b'Dutch')])),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('project_start', models.DateField()),
                ('is_ended', models.BooleanField(default=False)),
                ('project_end', models.DateField(blank=True)),
                ('developer', models.ForeignKey(related_name='developer', to='developers.Developer')),
            ],
        ),
    ]
