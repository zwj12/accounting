import logging

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import generic

from cash.forms import AccountingSubjectForm
from cash.models import AccountingSubject, CashOnHand

logger = logging.getLogger(__name__)


class IndexView(generic.ListView):
    template_name = 'cash/index.html'
    context_object_name = 'accounting_subject_list'

    def get_queryset(self):
        return AccountingSubject.objects.all()


class CashIndexView(generic.ListView):
    template_name = 'cash/cashindex.html'
    context_object_name = 'cash_list'

    def get_queryset(self):
        return CashOnHand.objects.all()


class DetailView(generic.DetailView):
    model = AccountingSubject
    context_object_name = 'accounting_subject'
    template_name = 'cash/detail.html'


def index(request):
    accounting_subject_list = AccountingSubject.objects.all()
    context = {'accounting_subject_list': accounting_subject_list}
    return render(request, 'cash/index.html', context)


def detail(request, accounting_subject_id):
    accounting_subject = get_object_or_404(AccountingSubject, pk=accounting_subject_id)
    return render(request, 'cash/detail.html', {'accounting_subject': accounting_subject})


def child(request):
    return render(request, 'cash/child.html')


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


def results(request, accounting_subject_id):
    return HttpResponse("You're looking at the results of accounting subject %s." % accounting_subject_id)

