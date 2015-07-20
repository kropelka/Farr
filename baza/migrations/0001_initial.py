# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adres',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('ulica', models.CharField(max_length=60)),
                ('numer', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Firma',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nazwa', models.CharField(blank=True, max_length=60)),
                ('www', models.CharField(max_length=100)),
                ('uwagi', models.TextField(blank=True)),
                ('adres', models.ForeignKey(to='baza.Adres', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Miejscowosc',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('imie', models.CharField(max_length=30)),
                ('nazwisko', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Telefon',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('numer', models.CharField(max_length=20)),
                ('rodzaj', models.CharField(max_length=5)),
                ('firma', models.ForeignKey(to='baza.Firma')),
                ('osoba', models.ForeignKey(to='baza.Osoba', blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='firma',
            name='wlasciciel',
            field=models.ForeignKey(to='baza.Osoba', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='adres',
            name='miejscowosc',
            field=models.ForeignKey(to='baza.Miejscowosc'),
        ),
    ]
