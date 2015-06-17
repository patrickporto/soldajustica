# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(blank=True, verbose_name='Tí\xadtulo', max_length=40)),
                ('description', models.CharField(blank=True, verbose_name='Descrição', max_length=140)),
                ('image', models.ImageField(height_field=500, upload_to='', verbose_name='Imagem', width_field=1200)),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('url', models.URLField()),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('last_update', models.DateTimeField(verbose_name='Data de Atualização', auto_now=True)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
