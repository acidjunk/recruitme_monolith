# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0005_allow_empty_github'),
    ]

    operations = [
        migrations.RenameField(
            model_name='developer',
            old_name='bio_en',
            new_name='bio_en_us',
        ),
        migrations.RenameField(
            model_name='developer',
            old_name='bio_nl',
            new_name='bio_nl_nl',
        ),
        migrations.AlterField(
            model_name='project',
            name='language',
            field=models.CharField(max_length=20, choices=[('en-us', 'English'), ('nl-nl', 'Dutch')]),
        ),
    ]
