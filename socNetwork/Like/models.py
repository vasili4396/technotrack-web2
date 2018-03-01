from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from Core.models import AuthorMixin, ShowMixin, DateTimeMixin


class Like (AuthorMixin, ShowMixin, DateTimeMixin):
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType)
    object = GenericForeignKey(ct_field='content_type', fk_field='object_id')

    def not_to_show(self):
        self.to_show = False
        super(Like, self).save()

    def get_title(self):
        return "%s liked %s of %s" % (self.author.get_author(),
                                      self.object.__class__.__name__.lower(),
                                      self.object.__class__.objects.get(pk=self.object_id).get_author(),
                                      )
    # avatar case: self.object.__class__.objects.get(pk=self.object_id).user.first_name
    # comment, post case: self.object.__class__.objects.get(pk=self.object_id).get_author()


class LikeMixin (models.Model):
    likes = GenericRelation(Like)
    likes_count = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True
