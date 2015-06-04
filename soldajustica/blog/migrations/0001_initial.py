# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(verbose_name='title', max_length=255)),
                ('content', models.TextField(verbose_name='content')),
                ('published', models.BooleanField(default=False, verbose_name='published')),
                ('pub_date', models.DateTimeField(verbose_name='publish date', blank=True)),
                ('date_created', models.DateTimeField(verbose_name='date created', auto_now_add=True)),
                ('last_update', models.DateTimeField(verbose_name='last update', auto_now=True)),
                ('author', models.ForeignKey(verbose_name='author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_created'],
                'get_latest_by': 'pub_date',
            },
        ),
    ]
