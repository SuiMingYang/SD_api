# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20151130_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='sdmodel',
            name='c',
            field=models.CharField(default=b'', max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='sdmodel',
            name='s',
            field=models.CharField(default=b'', max_length=10, blank=True),
        ),
    ]
