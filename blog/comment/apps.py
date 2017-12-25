from django.apps import AppConfig


class CommentsConfig(AppConfig):
    name = 'comment'

    def ready(self):
        print(__class__.__name__ + ' is ready')