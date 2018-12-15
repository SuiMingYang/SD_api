# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0010_sdmodel_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sdmodel',
            name='fname',
        ),
        migrations.AlterField(
            model_name='sdmodel',
            name='table',
            field=models.TextField(),
        ),
    ]
