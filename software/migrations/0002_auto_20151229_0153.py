# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='student',
            new_name='students',
        ),
        migrations.RemoveField(
            model_name='course',
            name='teacher',
        ),
        migrations.AlterField(
            model_name='course',
            name='classroom',
            field=models.CharField(max_length=30),
        ),
    ]
