from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from investment.models import CreateInvest


class CreateInvestForm(forms.ModelForm):

    class Meta:
        model = CreateInvest
        fields = (
            'base_currency','target_currency',
            'target_date', 'description',
            'token', 'analysis'
        )
        widgets = {
            'base_currency': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'target_currency': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'target_date': forms.SelectDateWidget(attrs={'class': 'form-control bg-transparent text-light', 'required': 'required', 'style': 'width: 25%; display: inline-block;'}),
            'description': forms.Textarea(attrs={'class': 'form-control bg-transparent text-light', 'required': 'required', 'placeholder': 'Description is little information. You should not give critical content of advice. This analysis must be satisfy.'}),
            'analysis': forms.Textarea(attrs={'class': 'form-control bg-transparent text-light', 'placeholder': 'Write an analysis for your advice buyers.'}),
            'token': forms.NumberInput(attrs={'class': 'form-control bg-transparent text-light', 'style': 'width: 86%; display: inline-block;'}),
        }

    def clean_target_date(self):
        value = self.cleaned_data['target_date']
        if value <= date.today():
            raise ValidationError(
                'Target date cannot be previous date and today.')
        return value