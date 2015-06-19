# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Nome', max_length=255)),
                ('description', models.CharField(verbose_name='Descrição', max_length=255, blank=True)),
                ('date_created', models.DateTimeField(verbose_name='Data de criação', auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')),
            ],
            options={
                'verbose_name': 'Galeria',
                'verbose_name_plural': 'Galerias',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('description', models.CharField(verbose_name='Descrição', max_length=140, blank=True)),
                ('image', models.ImageField(verbose_name='Imagem', upload_to='')),
                ('date_created', models.DateTimeField(verbose_name='Data de criação', auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')),
            ],
            options={
                'verbose_name': 'Imagem de Galeria',
                'verbose_name_plural': 'Imagens de Galeria',
                'ordering': ['-date_created'],
            },
        ),
        migrations.AddField(
            model_name='gallery',
            name='images',
            field=models.ManyToManyField(verbose_name='Imagens', related_name='galeries', to='gallery.GalleryImage'),
        ),
    ]
