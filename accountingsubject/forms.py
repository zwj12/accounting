from django.forms import ModelForm

from accountingsubject.models import AccountingSubject


class AccountingSubjectForm(ModelForm):
    class Meta:
        model = AccountingSubject
        fields = ['accounting_subject', 'debit_balance', 'remark']