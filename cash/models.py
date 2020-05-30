import datetime
from datetime import date

from django.db import models

# Create your models here.
from django.utils import timezone


class CommonInfo(models.Model):
    remark = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField('date created', auto_now_add=True)
    modified = models.DateTimeField('date modified', auto_now=True)

    class Meta:
        abstract = True


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


class CashOnHand(CommonInfo):
    operation_date = models.DateField(default=date.today)
    serial_number = models.IntegerField(default=1)
    lucre = models.FloatField()
    balance = models.FloatField(editable=False)
    summary = models.CharField(max_length=255)
    opposite_account = models.ForeignKey(AccountingSubject, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cash_cash_on_hand'

    def __str__(self):
        return self.summary

    def was_created_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)

    def save(self, *args, **kwargs):
        # do_something()
        super().save(*args, **kwargs)  # Call the "real" save() method.
        # do_something_else()
