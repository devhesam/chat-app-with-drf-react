from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from utils.base_models import BaseModel


class Category(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=155)
    description = models.TextField(verbose_name=_('description'), null=True, blank=True)

    def __str__(self):
        return self.name


class Server(BaseModel):
    name = models.CharField(verbose_name=_('name'), max_length=155)
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name=_('owner'), on_delete=models.CASCADE,
                              related_name='server_owner')
    category = models.ForeignKey(to=Category, verbose_name=_('category'), on_delete=models.CASCADE,
                                 related_name='server_category')
    description = models.CharField(verbose_name=_('description'), max_length=250, blank=True)
    member = models.ManyToManyField(to=settings.AUTH_USER_MODEL)
    is_active = models.BooleanField(verbose_name=_('is active'), default=True)

    def __str__(self):
        return self.name


class Channel(BaseModel):
    name = models.CharField(verbose_name=_('name'), max_length=155)
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name=_('owner'), on_delete=models.CASCADE,
                              related_name='channel_owner')
    topic = models.CharField(verbose_name=_('topic'), max_length=250)
    server = models.ForeignKey(to=Server, verbose_name=_('server'), on_delete=models.CASCADE,
                               related_name='channel_server')
    is_active = models.BooleanField(verbose_name=_('is active'), default=True)

    def __str__(self):
        return self.name
