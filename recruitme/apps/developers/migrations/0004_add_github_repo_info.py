# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0003_auto_20150810_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='github_repo_info',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='language',
            field=models.CharField(max_length=20, choices=[('en', 'English'), ('nl', 'Dutch')]),
        ),
    ]
