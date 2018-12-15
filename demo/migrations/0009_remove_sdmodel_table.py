# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0008_sdmodel_fname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sdmodel',
            name='table',
        ),
    ]
