from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from Core.models import AuthorMixin, ShowMixin, DateTimeMixin, EventMixin


class Like (AuthorMixin, ShowMixin, DateTimeMixin, EventMixin):
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object = GenericForeignKey(ct_field='content_type', fk_field='object_id')

    def not_to_show(self):
        self.to_show = False
        super(Like, self).save()

    def get_title(self):
        if hasattr(self.object.__class__.objects.get(pk=self.object_id), 'text'):
            ins_text = ": " + self.object.__class__.objects.get(pk=self.object_id).text
        else:
            ins_text = ''
        return "%s liked %s of %s" % (self.get_author().first_name,
                                      self.object.__class__.__name__.lower(),
                                      self.object.__class__.objects.get(pk=self.object_id).get_author().first_name,
                                      ) + ins_text
    # avatar case: self.object.__class__.objects.get(pk=self.object_id).user.first_name
    # comment, post case: self.object.__class__.objects.get(pk=self.object_id).get_author()


class LikeMixin (models.Model):
    likes = GenericRelation(Like)
    likes_count = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True
