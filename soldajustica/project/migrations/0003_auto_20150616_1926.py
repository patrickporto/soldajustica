# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20150615_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='active',
            field=models.BooleanField(verbose_name='Ativo', default=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(verbose_name='Data de criaÃ§Ã£o', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(verbose_name='DescriÃ§Ã£o'),
        ),
        migrations.AlterField(
            model_name='project',
            name='last_update',
            field=models.DateTimeField(verbose_name='Data de AtualizaÃ§Ã£o', auto_now=True),
        ),
    ]
