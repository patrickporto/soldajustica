from django.utils.translation import ugettext as _
from django.db import models


class MinistryMember(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Nome'))
    photo = models.ImageField(verbose_name=_('Foto'))
    description = models.TextField(verbose_name=_('Descrição'), blank=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Data de criação'))
    last_update = models.DateTimeField(auto_now=True, verbose_name=_('Data de Atualização'))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_created']
        verbose_name = _('Membro do Ministério')
        verbose_name_plural = _('Membros do Ministério')


class Ministry(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Nome'))
    slug = models.SlugField(verbose_name=_('Endereço'))
    description = models.TextField(verbose_name=_('Descrição'), blank=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Data de criação'))
    last_update = models.DateTimeField(auto_now=True, verbose_name=_('Data de Atualização'))

    members = models.ManyToManyField('MinistryMember', verbose_name=_("Membros"), related_name="ministries")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_created']
        verbose_name = _('Ministério')
        verbose_name_plural = _('Ministérios')