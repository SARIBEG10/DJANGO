from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)   # post_save means : when we click the Sign Up button in registered form data is
# posted by http post method to the built-in model
def build_profile(sender, instance, created, **kwargs):
    if created:     # this means : if user is registered and created
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()