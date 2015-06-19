# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='description',
            field=models.CharField(verbose_name='Descrição', max_length=140),
        ),
    ]
