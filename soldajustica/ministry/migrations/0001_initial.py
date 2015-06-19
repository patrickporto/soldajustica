# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ministry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('slug', models.SlugField(verbose_name='Endereço')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('date_created', models.DateTimeField(verbose_name='Data de criação', auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')),
            ],
            options={
                'ordering': ['-date_created'],
                'verbose_name': 'Ministério',
                'verbose_name_plural': 'Ministérios',
            },
        ),
        migrations.CreateModel(
            name='MinistryMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('photo', models.ImageField(verbose_name='Foto', upload_to='')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('date_created', models.DateTimeField(verbose_name='Data de criação', auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')),
            ],
            options={
                'ordering': ['-date_created'],
                'verbose_name': 'Membro do Ministério',
                'verbose_name_plural': 'Membros do Ministério',
            },
        ),
    ]
