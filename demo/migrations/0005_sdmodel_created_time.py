# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import demo.common.timefile


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_sdmodel_b'),
    ]

    operations = [
        migrations.AddField(
            model_name='sdmodel',
            name='created_time',
            field=models.DateTimeField(default=demo.common.timefile.get_now_time),
        ),
    ]
