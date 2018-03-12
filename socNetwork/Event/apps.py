from django.apps import AppConfig


class EventConfig(AppConfig):
    name = 'Event'

    def ready(self):
        import Event.signals
        # print('Comment is ready')
