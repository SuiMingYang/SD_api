# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0011_auto_20151224_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='sdmodel',
            name='rand_fname',
            field=models.CharField(default=b'', max_length=20, blank=True),
        ),
    ]
