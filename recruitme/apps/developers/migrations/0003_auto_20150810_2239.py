# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0002_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_start',
            new_name='start',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_end',
        ),
        migrations.AddField(
            model_name='project',
            name='end',
            field=models.DateField(null=True, blank=True),
        ),
    ]
