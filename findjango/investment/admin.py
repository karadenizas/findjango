from django.contrib import admin
from investment.models import CreateInvest

@admin.register(CreateInvest)
class CreateInvestAdmin(admin.ModelAdmin):
    list_display = ['investor', 'base_currency', 'target_currency', 'target_value', 'token']