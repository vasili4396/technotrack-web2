from __future__ import unicode_literals


class EventMixin:
    def get_title(self):
        raise NotImplementedError

    def get_author(self):
        raise NotImplementedError
