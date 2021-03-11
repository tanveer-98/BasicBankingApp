from django import forms
from app1.models import customer

class TransferForm(forms.Form):
    name = forms.CharField(max_length=200)
    amount = forms.IntegerField()
