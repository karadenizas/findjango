from django.db import models

from userprofile.models import MyUser


class UserWallet(models.Model):
    user = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='wallet'
    )
    token = models.IntegerField(default=0)

    def __str__(self):
        return self.user.user_name


class PaymentTransaction(models.Model):
    wallet = models.ForeignKey(
        UserWallet,
        on_delete=models.CASCADE,
        related_name='transactions')
    transaction_type = models.CharField(
        max_length=10,
        choices=(
        ('buy', 'Buying Transactions'), ('sell', 'Selling Transactions'),))
    braintree_id = models.CharField(max_length=150, blank=True)
    # you can change the other integerfields to positiveintegerfield
    amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.wallet.user.user_name


class PurchaseOption(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500, default='')
    token_amount = models.IntegerField(default=0)
    token_price = models.DecimalField(
        max_digits=5, decimal_places=2, default=0)
    total_price = models.DecimalField(
        max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.total_price = self.token_amount * self.token_price
        return super().save(*args, **kwargs)
