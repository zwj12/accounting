from django import forms
from django.forms import ModelForm

from cash.models import CashOnHand


# class AccountingSubjectForm(forms.Form):
#     accounting_subject = forms.CharField(label='accounting subject', max_length=50)
#     debit_balance = forms.BooleanField(label='debit balance', required=False)
#     remark = forms.CharField(label='remark subject', max_length=255)


class CashOnHandForm(ModelForm):
    class Meta:
        model = CashOnHand
        # fields = ['operation_date', 'serial_number', 'opposite_account', 'summary', 'lucre', 'balance', 'remark']
        fields = ['operation_date', 'serial_number', 'opposite_account', 'summary', 'lucre', 'remark']
