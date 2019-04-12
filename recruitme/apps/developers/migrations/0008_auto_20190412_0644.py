# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0007_merge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='developer',
            old_name='bio_en_us',
            new_name='bio_en',
        ),
        migrations.RenameField(
            model_name='developer',
            old_name='bio_nl_nl',
            new_name='bio_nl',
        ),
        migrations.AlterField(
            model_name='project',
            name='language',
            field=models.CharField(max_length=20, choices=[('en', 'English'), ('nl', 'Dutch')]),
        ),
    ]
