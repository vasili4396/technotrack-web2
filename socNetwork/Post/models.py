from __future__ import unicode_literals

from django.db import models
from Core.models import AuthorMixin, PublicationMixin, DateTimeMixin, ShowMixin
from Comment.models import CommentMixin
from Like.models import LikeMixin


class Post (AuthorMixin, PublicationMixin, DateTimeMixin,
            CommentMixin, LikeMixin, ShowMixin):
    title = models.CharField(max_length=255)

    # TODO: доделать нормально

    def get_title(self):
        return "%s posted %s" %\
               (self.get_author(),
                self.title[0:15:1],
                )
