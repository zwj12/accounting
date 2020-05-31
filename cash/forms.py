from django import forms


class AccountingSubjectForm(forms.Form):
    accounting_subject = forms.CharField(label='accounting subject', max_length=50)
    debit_balance = forms.BooleanField(label='debit balance', required=False)
    remark = forms.CharField(label='remark subject', max_length=255)
