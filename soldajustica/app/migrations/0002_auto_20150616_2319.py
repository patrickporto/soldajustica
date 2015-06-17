# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(verbose_name='Imagem', upload_to=''),
        ),
        migrations.AlterField(
            model_name='slide',
            name='title',
            field=models.CharField(verbose_name='Tí\xadtulo', max_length=40),
        ),
    ]
