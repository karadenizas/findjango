from django.db import models
from userprofile.models import MyUser


class UserWallet(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='wallet')
    token = models.IntegerField(default=0)

    def __str__(self):
        return self.user.user_name


class PurchaseOption(models.Model):
    name = models.CharField(max_length=255)
    token_amount = models.IntegerField(default=0)

    def __str__(self):
        return self.name