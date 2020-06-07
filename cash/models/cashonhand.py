import datetime
from datetime import date
from django.utils import timezone
from django.db import models
from cash.models import CommonInfo
from cash.models import AccountingSubject


class CashOnHand(CommonInfo):
    operation_date = models.DateField(default=date.today)
    serial_number = models.IntegerField("sequence", default=1)
    lucre = models.FloatField()
    # balance = models.FloatField(editable=False)
    balance = models.FloatField()
    summary = models.CharField(max_length=255)
    opposite_account = models.ForeignKey(AccountingSubject, on_delete=models.CASCADE, verbose_name="subject")

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
