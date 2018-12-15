# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_sdmodel_created_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sdmodel',
            name='created_time',
            field=models.DateTimeField(default=b''),
        ),
    ]
