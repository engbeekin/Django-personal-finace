from django import forms
from django.forms import ModelForm

from category.models import Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-sm rounded'}),
        }