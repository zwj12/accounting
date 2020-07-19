from django.db.models import Count, Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import generic

from accountingsubject.forms import AccountingSubjectForm
from accountingsubject.models import AccountingSubject
from cash.models import CashOnHand


class IndexView(generic.ListView):
    template_name = 'accountingsubject/index.html'
    context_object_name = 'accounting_subject_list'

    def get_queryset(self):
        return AccountingSubject.objects.annotate(Count('cashonhand'), Sum('cashonhand__lucre'))


class DetailView(generic.DetailView):
    model = AccountingSubject
    context_object_name = 'accounting_subject'
    template_name = 'accountingsubject/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_count'] = CashOnHand.objects.filter(opposite_account_id=self.object.id).count()
        context['list_sum'] = CashOnHand.objects.filter(opposite_account_id=self.object.id).count()
        return context


# @login_required()
def accounting_subject_edit(request, accounting_subject_id):
    # logger.error(request)
    # if request.user.is_authenticated:
    #     # A backend authenticated the credentials
    #     logger.debug(request.user.username + " is logged")
    #     if request.user.has_perm('cash.add_cashonhand'):
    #         logger.debug(request.user.username + " has permission: cash.add_cashonhand")
    #     if request.user.has_perm('cash.add_accountingsubject'):
    #         logger.debug(request.user.username + " has permission: cash.add_accountingsubject")
    #     return HttpResponseRedirect('/admin')
    # else:
    #     # No backend authenticated the credentials
    #     return HttpResponseRedirect('/cash')

    accounting_subject = get_object_or_404(AccountingSubject, pk=accounting_subject_id)
    if request.method == 'POST':
        form = AccountingSubjectForm(request.POST)
        if form.is_valid():
            accounting_subject.accounting_subject = form.cleaned_data['accounting_subject']
            accounting_subject.debit_balance = form.cleaned_data['debit_balance']
            accounting_subject.remark = form.cleaned_data['remark']
            accounting_subject.save()
            # return render(request, 'cash/accountingsubjectedit.html',
            #               {'form': form, 'accounting_subject': accounting_subject})
            return HttpResponseRedirect('/cash')
    else:
        obj = {"accounting_subject":accounting_subject.accounting_subject,
               "debit_balance":accounting_subject.debit_balance,
               "remark": accounting_subject.remark,
               }
        form = AccountingSubjectForm(obj)

    return render(request, 'cash/accountingsubjectedit.html', {'form': form, 'accounting_subject': accounting_subject})