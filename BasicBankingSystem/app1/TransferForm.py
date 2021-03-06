from django import forms
from app1.models import customer

class TransferForm(forms.Form):
    amount = forms.IntegerField()
