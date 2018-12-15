# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0009_remove_sdmodel_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='sdmodel',
            name='table',
            field=models.TextField(default=b''),
        ),
    ]
