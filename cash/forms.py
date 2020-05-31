from django import forms


class AccountingSubjectForm(forms.Form):
    accounting_subject = forms.CharField(label='accounting subject', max_length=50)
