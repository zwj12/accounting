from django.db import models

# Create your models here.
from cash.models import CommonInfo


class AccountingSubject(CommonInfo):
    # Note that when unique is True,
    # you don’t need to specify db_index,
    # because unique implies the creation of an index.
    accounting_subject = models.CharField(max_length=50, unique=True, help_text="会计科目")
    debit_balance = models.BooleanField(default=True)

    class Meta:
        db_table = 'cash_accounting_subject'

    def __str__(self):
        return self.accounting_subject
