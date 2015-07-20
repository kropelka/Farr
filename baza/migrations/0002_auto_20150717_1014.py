# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='telefon',
            name='czy_podstawowy',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='firma',
            name='www',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
