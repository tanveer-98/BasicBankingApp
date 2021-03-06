from django import forms
from app1.models import customer

class TransferForm(forms.Form):
    transferTo = forms.IntegerField()
    amount = forms.IntegerField()
