from django.db.models.signals import post_save, post_init
from django.dispatch import receiver
from .models import Avatar


@receiver(post_save, sender=Avatar)
def modify_avatar(instance, created=False, **kwargs):
    if created:
        instance.__class__.objects.filter(pk=instance.id).update(to_show=True)


