from django.contrib import admin
from investment.models import CreateInvest, ResultInvest

@admin.register(CreateInvest)
class CreateInvestAdmin(admin.ModelAdmin):
    list_display = ['investor', 'base_currency', 'target_currency', 'target_value', 'token', 'active', 'target_date']


@admin.register(ResultInvest)
class ResultInvestAdmin(admin.ModelAdmin):
    list_display = ['invest', 'investor', 'start_value', 'result_value']