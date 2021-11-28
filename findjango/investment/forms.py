from django import forms
from investment.models import CreateInvest
from datetime import date

class CreateInvestForm(forms.ModelForm):

    class Meta:
        model = CreateInvest
        fields = ('base_currency','target_currency', 'target_date', 'description', 'token', 'analysis')
        widgets = {
            'base_currency': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'target_currency': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'target_date': forms.SelectDateWidget(attrs={'class': 'form-control bg-transparent text-light', 'required': 'required', 'style': 'width: 25%; display: inline-block;'}),
            'description': forms.Textarea(attrs={'class': 'form-control bg-transparent text-light', 'required': 'required', 'placeholder': 'Description is little information. You should not give critical content of advice. This analysis must be satisfy.'}),
            'analysis': forms.Textarea(attrs={'class': 'form-control bg-transparent text-light', 'placeholder': 'Write an analysis for your advice buyers.'}),
            'token': forms.NumberInput(attrs={'class': 'form-control bg-transparent text-light', 'style': 'width: 86%; display: inline-block;'}),
        }