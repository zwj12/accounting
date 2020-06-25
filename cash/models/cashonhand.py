import datetime
from datetime import date

from django.urls import reverse
from django.utils import timezone
from django.db import models

from accountingsubject.models import AccountingSubject
from cash.models import CommonInfo


class CashOnHand(CommonInfo):
    operation_date = models.DateField(default=date.today)
    serial_number = models.IntegerField("sequence", default=1)
    lucre = models.FloatField()
    balance = models.FloatField(editable=False)
    # balance = models.FloatField()
    summary = models.CharField(max_length=255)
    opposite_account = models.ForeignKey(AccountingSubject, on_delete=models.CASCADE, verbose_name="subject")

    class Meta:
        db_table = 'cash_cash_on_hand'
        ordering = ['operation_date', 'serial_number']

    def __str__(self):
        return self.summary

    def was_created_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)

    def get_absolute_url(self):
        return reverse('cash:detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        # do_something()
        if "bool_adjust_balance" in kwargs:
            bool_adjust_balance = kwargs["bool_adjust_balance"]
            kwargs.pop("bool_adjust_balance")
        else:
            bool_adjust_balance = True
        if self.balance is None:
            self.balance = 0
        super().save(*args, **kwargs)  # Call the "real" save() method.
        # do_something_else()
        if bool_adjust_balance:
            self.adjust_balance()

    def adjust_serial_number(self):
        cash_on_hands = CashOnHand.objects.filter(
            operation_date=self.operation_date).order_by('serial_number', 'modified')
        serial_number_next = 1
        for cash_on_hand in cash_on_hands:
            cash_on_hand.serial_number = serial_number_next
            cash_on_hand.save(bool_adjust_balance=False)
            # cash_on_hand.save()
            serial_number_next = serial_number_next + 1

    def adjust_balance(self):
        self.adjust_serial_number()
        cash_on_hands = CashOnHand.objects.filter(
            operation_date__gte=self.operation_date).order_by('operation_date', 'serial_number')
        try:
            cash_on_hand_pre = CashOnHand.objects.filter(
                operation_date__lt=self.operation_date).order_by('-operation_date', '-serial_number')[0]
            balance_pre = cash_on_hand_pre.balance
        except IndexError:
            balance_pre = 0

        for cash_on_hand in cash_on_hands:
            if cash_on_hand.opposite_account.debit_balance:
                cash_on_hand.balance = balance_pre - cash_on_hand.lucre
            else:
                cash_on_hand.balance = balance_pre + cash_on_hand.lucre
            # cash_on_hand.save()
            cash_on_hand.save(bool_adjust_balance=False)
            balance_pre = cash_on_hand.balance
