from django.db.models.signals import post_save
from django.dispatch import receiver

from userprofile.models import MyUser
from payment.models import UserWallet


@receiver(post_save, sender=MyUser)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        UserWallet.objects.create(user=instance)