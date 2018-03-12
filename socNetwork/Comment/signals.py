from django.db.models.signals import post_save, post_delete, pre_save
from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
from django.db.models import F
from .models import Comment


@receiver(pre_save, sender=Comment)
def to_show_before_save(instance, **kwargs):
    if instance.__class__.objects.filter(pk=instance.id).exists():
        instance.to_show_before_save = instance.__class__.objects.get(pk=instance.id).to_show
    else:
        instance.to_show_before_save = False


@receiver(post_save, sender=Comment)
def update_comment(instance, update_fields=None, created=False, **kwargs):

    try:
        instance.to_show_iwant
    except AttributeError:
        instance.to_show_iwant = instance.to_show

    if instance.object.__class__.objects.get(pk=instance.object_id).to_show:
        if created:
            instance.object.__class__.objects.filter(pk=instance.object_id).update(
                comments_count=F('comments_count') + 1
            )
            instance.__class__.objects.filter(pk=instance.id).update(to_show=True)
        if not created:
            if instance.to_show_iwant:                                    # became True
                if instance.to_show_before_save:                          # was True
                    instance.__class__.objects.filter(pk=instance.id).update()
                else:                                                     # was False
                    instance.__class__.objects.filter(pk=instance.id).update(to_show=True)
                    instance.object.__class__.objects.filter(pk=instance.object_id).update(
                        comments_count=F('comments_count') + 1
                    )
            else:                                                         # became False
                if instance.to_show_before_save:                          # was True
                    instance.__class__.objects.filter(pk=instance.id).update(to_show=False)
                    instance.object.__class__.objects.filter(pk=instance.object_id).update(
                        comments_count=F('comments_count') - 1
                    )
                else:                                                     # was False
                    pass
    else:
        raise Exception('object was deleted or has not been created yet ')


@receiver(post_delete, sender=Comment)
def delete_comment(instance, **kwargs):
    if instance.object.__class__.objects.get(pk=instance.object_id).to_show:
        instance.object.__class__.objects.filter(pk=instance.object_id).update(comments_count=F('comments_count') - 1)
    else:
        raise Exception('object has already been deleted or has not been created yet ')
