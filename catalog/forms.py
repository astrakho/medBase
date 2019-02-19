import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class AddForm(forms.Form):
    search = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_search(self):
        clean_search = self.cleaned_data['search']
        if len(clean_search) > 50:
            raise ValidationError('The input is too big', code = 'invalid')
        return clean_search






class SubmitForm(forms.Form):
    code = forms.CharField(max_length = 10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    quantity = forms.CharField(max_length = 3, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_search(self):
        clean_search = self.cleaned_data['search']
        if len(clean_search) > 25:
            raise ValidationError('The input is too big', code = 'invalid')
        return clean_search

