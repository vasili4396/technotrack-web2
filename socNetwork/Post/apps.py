from django.apps import AppConfig


class PostConfig(AppConfig):
    name = 'Post'

    def ready(self):
        import Post.signals
        # print('Post is ready')
