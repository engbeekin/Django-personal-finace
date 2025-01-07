from django.forms import ModelForm
from django import forms
from accounts.models import Account


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ('name','balance')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-sm rounded'}),
            'balance': forms.TextInput(attrs={'class': 'form-control form-control-sm rounded'}),
        }