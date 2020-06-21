from django.contrib import admin

# Register your models here.
from accountingsubject.models import AccountingSubject


class AccountingSubjectAdmin(admin.ModelAdmin):
    fields = ['accounting_subject', 'debit_balance', 'remark']
    list_display = ('accounting_subject', 'debit_balance', 'remark')


admin.site.register(AccountingSubject, AccountingSubjectAdmin)