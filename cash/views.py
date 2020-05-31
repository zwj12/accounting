from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import generic

from cash.forms import AccountingSubjectForm
from cash.models import AccountingSubject


class IndexView(generic.ListView):
    template_name = 'cash/index.html'
    context_object_name = 'accounting_subject_list'

    def get_queryset(self):
        return AccountingSubject.objects.all()


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


def accounting_subject_edit(request, accounting_subject_id):
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

