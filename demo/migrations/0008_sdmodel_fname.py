# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_auto_20151208_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='sdmodel',
            name='fname',
            field=models.CharField(default=b'', max_length=20, blank=True),
        ),
    ]
