# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0002_auto_20150717_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='adres',
            name='przedrostek',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
