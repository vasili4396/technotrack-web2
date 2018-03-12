from django.db.models.signals import pre_save, pre_init, post_save

from Event.models import Event
from Core.models import EventMixin


def saving_eventable_model(instance, created=False, **kwargs):
    event = Event(title=instance.get_title(),
                  author=instance.get_author(),
                  to_show=True,
                  )
    event.save()


for model in EventMixin.__subclasses__():
    post_save.connect(saving_eventable_model, sender=model)