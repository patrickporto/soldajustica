from django.utils.translation import ugettext as _
from django.db import models


class Slide(models.Model):
    title = models.CharField(max_length=40, verbose_name=_('Tí­tulo'))
    description = models.CharField(max_length=140, blank=True, verbose_name=_('Descrição'))
    image = models.ImageField(verbose_name=_('Imagem'))
    active = models.BooleanField(default=True, verbose_name=_('Ativo'))
    url = models.URLField()
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Data de criação'))
    last_update = models.DateTimeField(auto_now=True, verbose_name=_('Data de Atualização'))

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_created']