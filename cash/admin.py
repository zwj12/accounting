from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import CashOnHand


class CashOnHandAdmin(admin.ModelAdmin):
    # fields = ['operation_date', 'serial_number', 'opposite_account', 'summary', 'lucre', 'balance', 'remark']
    fields = ['operation_date', 'serial_number', 'opposite_account', 'summary', 'lucre', 'remark']
    list_display = ('operation_date', 'serial_number', 'opposite_account', 'summary', 'lucre', 'balance', 'remark')
    list_filter = ['operation_date']
    search_fields = ['summary']


admin.site.register(CashOnHand, CashOnHandAdmin)