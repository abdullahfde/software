# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0004_auto_20151229_0158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='teachers',
        ),
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to='software.student'),
        ),
    ]
