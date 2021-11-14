from typing import DefaultDict
from django import forms
from django.db.models.enums import Choices
from django.forms import fields
from investment.models import CreateInvest


class CreateInvestForm(forms.ModelForm):

    class Meta:
        model = CreateInvest
        fields = (
                  'base_currency','target_currency', 'target_date')
        widgets = {
            'base_currency': forms.TextInput(attrs={'class': 'form-control'}),
            'target_currency': forms.TextInput(attrs={'class': 'form-control'}),
            'target_date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
        }
        