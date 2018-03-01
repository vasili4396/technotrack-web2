from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from Core.models import AuthorMixin, PublicationMixin, DateTimeMixin, ShowMixin
from Like.models import LikeMixin


class Comment (AuthorMixin, PublicationMixin, DateTimeMixin, LikeMixin, ShowMixin):
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType)
    object = GenericForeignKey(ct_field='content_type', fk_field='object_id')

    def get_title(self):
        return "%s commented on %s of %s" % \
               (self.author.get_author(),
                self.object.__class__.__name__.lower(),
                self.object.__class__.objects.get(pk=self.object_id).get_author(),
                )


class CommentMixin (models.Model):
    comments = GenericRelation(Comment)
    comments_count = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True
