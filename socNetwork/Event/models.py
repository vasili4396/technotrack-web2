from __future__ import unicode_literals
from Core.models import *
from Like.models import LikeMixin
from Comment.models import CommentMixin


class Event(AuthorMixin, DateTimeMixin, ShowMixin, CommentMixin, LikeMixin):
    title = models.CharField(max_length=255, blank=True, null=True)

    def get_author(self):
        return self.author
