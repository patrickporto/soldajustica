# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('project', models.ImageField(verbose_name='Imagem', upload_to='')),
                ('active', models.BooleanField(verbose_name='Ativo')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')),
            ],
            options={
                'verbose_name': 'Projeto',
                'verbose_name_plural': 'Projetos',
                'ordering': ['-date_created'],
            },
        ),
    ]
