from django.utils.translation import ugettext as _
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Nome'))
    description = models.TextField(verbose_name=_('DescriÃ§Ã£o'))
    image = models.ImageField(verbose_name=_('Imagem'))
    active = models.BooleanField(verbose_name=_('Ativo'), default=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Data de criaÃ§Ã£o'))
    last_update = models.DateTimeField(auto_now=True, verbose_name=_('Data de AtualizaÃ§Ã£o'))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_created']
        verbose_name = _('Projeto')
        verbose_name_plural = _('Projetos')