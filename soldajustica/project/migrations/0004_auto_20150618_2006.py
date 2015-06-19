# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20150616_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(verbose_name='Data de criação', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='project',
            name='last_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Data de Atualização'),
        ),
    ]
