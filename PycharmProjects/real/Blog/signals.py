from django.db.models.signals import post_save
from django.dispatch import receiver

from Blog.models import Blog


@receiver(post_save, sender=Blog)
def add_owner(instance, created, **kwargs):
    if created:
        instance.members.add(instance.owner)
        instance.objects.using('test').all()
        instance.save()