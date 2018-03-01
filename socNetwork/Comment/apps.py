from django.apps import AppConfig

class CommentConfig(AppConfig):
    name = 'Comment'

    def ready(self):
        import Comment.signals
        # print('Comment is ready')
