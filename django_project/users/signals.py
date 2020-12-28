from django.contrib.auth.models import User  # sender of the signal
from django.db.models.signals import post_save  # signal
from django.dispatch import receiver

from .models import Profile


# Refer: https://docs.djangoproject.com/en/3.1/topics/signals/
# `post_save` signal is sent whenever a model is saved. However, this signal will be received only when the
# sender of this signal is `User`
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
