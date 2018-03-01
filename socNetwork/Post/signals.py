from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post


@receiver(post_save, sender=Post)
def modify_post(instance, update_fields=None, created=False, **kwargs):
    if created:
        instance.__class__.objects.filter(pk=instance.id).update(to_show=True)
    if not created:
        instance.__class__.objects.filter(pk=instance.id).update()


