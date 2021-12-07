from django.contrib import admin
from payment.models import PurchaseOption, UserWallet, PaymentTransaction


@admin.register(PurchaseOption)
class PurchaseOptionAdmin(admin.ModelAdmin):
    list_display = ['name', 'token_price', 'token_amount', 'total_price']


@admin.register(UserWallet)
class UserWalletAdmin(admin.ModelAdmin):
    list_display = ['user', 'token']


@admin.register(PaymentTransaction)
class PaymentTransactionAdmin(admin.ModelAdmin):
    list_display = ['wallet', 'transaction_type', 'amount', 'braintree_id']