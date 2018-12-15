# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0006_auto_20151208_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sdmodel',
            name='created_time',
            field=models.CharField(default=b'', max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='sdmodel',
            name='sdmethod',
            field=models.CharField(default=b'', max_length=10, blank=True),
        ),
    ]
