from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import AccountingSubject, CashOnHand, Choice


class AccountingSubjectAdmin(admin.ModelAdmin):
    fields = ['accounting_subject', 'debit_balance', 'remark']
    list_display = ('accounting_subject', 'debit_balance', 'remark')


class CashOnHandAdmin(admin.ModelAdmin):
    # fields = ['operation_date', 'serial_number', 'opposite_account', 'summary', 'lucre', 'balance', 'remark']
    fields = ['operation_date', 'serial_number', 'opposite_account', 'summary', 'lucre', 'remark']
    list_display = ('operation_date', 'serial_number', 'opposite_account', 'summary', 'lucre', 'balance', 'remark')
    list_filter = ['operation_date']
    search_fields = ['summary']


class ChoiceAdmin(admin.ModelAdmin):
    fields = ['choice_text', 'votes', 'serial_number', 'lucre']


admin.site.register(AccountingSubject, AccountingSubjectAdmin)
admin.site.register(CashOnHand, CashOnHandAdmin)
admin.site.register(Choice, ChoiceAdmin)