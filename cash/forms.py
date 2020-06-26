from datetime import date

from django import forms
from django.forms import ModelForm, Form

from cash.models import CashOnHand, AccountingSubject


# class AccountingSubjectForm(forms.Form):
#     accounting_subject = forms.CharField(label='accounting subject', max_length=50)
#     debit_balance = forms.BooleanField(label='debit balance', required=False)
#     remark = forms.CharField(label='remark subject', max_length=255)


class CashOnHandModelForm(ModelForm):
    class Meta:
        model = CashOnHand
        # fields = ['operation_date', 'serial_number', 'opposite_account', 'summary', 'lucre', 'balance', 'remark']
        fields = ['operation_date', 'serial_number', 'opposite_account', 'summary', 'lucre', 'remark']
        labels = {
            'operation_date': '入账日期',
        }
        help_texts = {
            'operation_date': '实际发生日期',
        }
        widgets = {
            'operation_date': forms.DateInput(attrs={'type': 'date'}),
        }


class CashOnHandForm(Form):
    operation_date = forms.DateField(label='日期')
    serial_number = forms.IntegerField(label="序号")
    lucre = forms.FloatField(label='金额')
    summary = forms.CharField(label='内容', max_length=255)
    opposite_account = forms.ChoiceField(label='会计科目')
    remark = forms.CharField(label='备注', max_length=255)

    class Meta:
        model = CashOnHand
