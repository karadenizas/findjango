from django.db.models.signals import post_save
from django.dispatch import receiver
from userprofile.models import MyUser, Profile
from django.utils.text import slugify


@receiver(post_save, sender=MyUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, slug=slugify(instance))