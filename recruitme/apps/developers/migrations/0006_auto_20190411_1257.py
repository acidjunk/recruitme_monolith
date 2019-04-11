# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0005_allow_empty_github'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='bitbucket_profile',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='developer',
            name='bitbucket_repo_info',
            field=models.TextField(blank=True),
        ),
    ]
