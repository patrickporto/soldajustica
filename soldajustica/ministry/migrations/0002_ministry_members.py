# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ministry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ministry',
            name='members',
            field=models.ManyToManyField(verbose_name='Membros', to='ministry.MinistryMember', related_name='ministries'),
        ),
    ]
