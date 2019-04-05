# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0004_add_github_repo_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='github_repo_info',
            field=models.TextField(blank=True),
        ),
    ]
