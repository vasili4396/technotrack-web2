from django.apps import AppConfig

class LikeConfig(AppConfig):
    name = 'Like'

    def ready(self):
        import Like.signals
        # print('Like is ready')
