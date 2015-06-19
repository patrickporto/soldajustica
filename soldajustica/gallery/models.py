from django.utils.translation import ugettext as _
from django.db import models


class GalleryImage(models.Model):
    description = models.CharField(max_length=140, verbose_name=_('Descrição'))
    image = models.ImageField(verbose_name=_('Imagem'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Data de criação'))
    last_update = models.DateTimeField(auto_now=True, verbose_name=_('Data de Atualização'))

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['-date_created']
        verbose_name = _('Imagem de Galeria')
        verbose_name_plural = _('Imagens de Galeria')


class Gallery(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Nome'))
    description = models.CharField(max_length=255, verbose_name=_('Descrição'), blank=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Data de criação'))
    last_update = models.DateTimeField(auto_now=True, verbose_name=_('Data de Atualização'))

    images = models.ManyToManyField('GalleryImage', verbose_name=_('Imagens'), related_name='galeries')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_created']
        verbose_name = _('Galeria')
        verbose_name_plural = _('Galerias')