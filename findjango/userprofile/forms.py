from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.forms import widgets
from userprofile.models import MyUser


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', 
                                widget=forms.PasswordInput(attrs={'name': 'no', 'placeholder': 'Password', 'class': 'form-control'}))
    password2 = forms.CharField(label='Password confirmation', 
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password Confirmation', 'class': 'form-control'}))

    class Meta:
        model = MyUser
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'user_name': forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
        }
        fields = ('email', 'user_name')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'user_name', 'password', 'is_active', 'is_admin')