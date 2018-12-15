# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_auto_20151207_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='sdmodel',
            name='b',
            field=models.CharField(default=b'', max_length=10, blank=True),
        ),
    ]
