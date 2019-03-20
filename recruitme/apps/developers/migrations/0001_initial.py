# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True)),
                ('birth_date', models.DateField()),
                ('bio', models.TextField()),
                ('bio_en', models.TextField(null=True)),
                ('bio_nl', models.TextField(null=True)),
                ('city', models.CharField(max_length=128)),
                ('is_public', models.BooleanField(default=False)),
                ('profile_title', models.CharField(max_length=255)),
                ('linkedin_profile', models.URLField(blank=True)),
                ('github_profile', models.URLField(blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(related_name='developer_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(related_name='developer_modified_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_on',),
                'get_latest_by': 'created_on',
                'verbose_name': 'developer',
            },
        ),
    ]
