from django.db.models.signals import post_delete, pre_save, post_save
from django.dispatch import receiver
from django.db.models import F
from .models import Like


@receiver(post_save, sender=Like)
def update_like(instance, created=False, **kwargs):
    if instance.object.__class__.objects.get(pk=instance.object_id).to_show:
        if created:
            instance.object.__class__.objects.filter(pk=instance.object_id).update(likes_count=F('likes_count')+1)
            instance.__class__.objects.filter(pk=instance.id).update(to_show=True)
        else:
            if instance.to_show:
                instance.object.__class__.objects.filter(pk=instance.object_id).update(likes_count=F('likes_count') - 1)
                instance.__class__.objects.filter(pk=instance.id).update(to_show=False)
            else:
                instance.object.__class__.objects.filter(pk=instance.object_id).update(likes_count=F('likes_count') + 1)
                instance.__class__.objects.filter(pk=instance.id).update(to_show=True)
    else:
        raise Exception('object was deleted or has not been created yet ')


@receiver(post_delete, sender=Like)
def delete_like(instance, **kwargs):
    if instance.object.__class__.objects.get(pk=instance.object_id).to_show:
        instance.object.__class__.objects.filter(pk=instance.object_id).update(likes_count=F('likes_count') - 1)
    else:
        raise Exception('object was deleted or has not been created yet ')
