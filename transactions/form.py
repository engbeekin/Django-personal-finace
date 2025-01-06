from django import  forms
from django.forms import ModelForm
from .models import Transaction


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ('account', 'category', 'type_of_transaction', 'Amount',
                  'description', 'status')
        exclude = ['created_by']

        widgets = {
            'account': forms.Select(attrs={'class': 'form-control form-control-sm rounded'}),
            'category': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'type_of_transaction': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'Amount': forms.TextInput(attrs={'class': 'form-control form-control-sm rounded'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-sm rounded'}),
            # 'status': forms.CheckboxInput(attrs={'class': 'form-control form-control-sm'})
        }


