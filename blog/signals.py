from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify
from .models import *


@receiver(pre_save, sender=Post)
def post_pre_save_receiver(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)