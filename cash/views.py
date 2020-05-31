from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from cash.forms import AccountingSubjectForm
from cash.models import AccountingSubject


def index(request):
    accounting_subject_list = AccountingSubject.objects.all()
    context = {'accounting_subject_list': accounting_subject_list}
    return render(request, 'cash/index.html', context)


def detail(request, accounting_subject_id):
    accounting_subject = get_object_or_404(AccountingSubject, pk=accounting_subject_id)
    return render(request, 'cash/detail.html', {'accounting_subject': accounting_subject})


def accounting_subject_edit(request, accounting_subject_id):
    if request.method == 'POST':
        form = AccountingSubjectForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/cash/')
    else:
        form = AccountingSubjectForm()

    return render(request, 'cash/accountingsubjectedit.html', {'form': form})


def results(request, accounting_subject_id):
    return HttpResponse("You're looking at the results of accounting subject %s." % accounting_subject_id)

