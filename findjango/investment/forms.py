from django import forms
from investment.models import CreateInvest


class CreateInvestForm(forms.ModelForm):

    class Meta:
        model = CreateInvest
        fields = ('base_currency','target_currency', 'target_date', 'description', 'token', 'analysis')
        widgets = {
            'base_currency': forms.TextInput(attrs={'class': 'form-control'}),
            'target_currency': forms.TextInput(attrs={'class': 'form-control'}),
            'target_date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'analysis': forms.Textarea(attrs={'class': 'form-control'}),
            'token': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        