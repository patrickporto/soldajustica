from django.utils.translation import ugettext as _
from django.db import models
from django.conf import settings
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    content = models.TextField(verbose_name=_('content'))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('author'))
    published = models.BooleanField(default=False, verbose_name=_('published'))
    pub_date = models.DateTimeField(verbose_name=_('publish date'), blank=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('date created'))
    last_update = models.DateTimeField(auto_now=True, verbose_name=_('last update'))

    def __str__(self):
        return self.title

    class Meta:
        get_latest_by = 'pub_date'
        ordering = ['-date_created']

    @staticmethod
    def pre_save(sender, instance, *args, **kwargs):
        if (instance.published == True):
            instance.pub_date = datetime.now()


models.signals.pre_save.connect(Post.pre_save, sender=Post)