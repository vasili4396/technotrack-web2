from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class PublicationMixin (models.Model):
    text = models.TextField()

    class Meta:
        abstract = True


class AuthorMixin (models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def get_author(self):
        return self.author

    class Meta:
        abstract = True


class ShowMixin (models.Model):
    to_show = models.BooleanField(default=False)

    class Meta:
        abstract = True


class DateTimeMixin (models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True


class EventMixin(models.Model):
    def get_title(self):
        raise NotImplementedError

    def get_author(self):
        raise NotImplementedError

    class Meta:
        abstract = True

