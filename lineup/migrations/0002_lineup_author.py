# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lineup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineup',
            name='author',
            field=models.CharField(default='Chris', max_length=100),
            preserve_default=False,
        ),
    ]
