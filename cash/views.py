import logging

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from cash.forms import CashOnHandForm, CashOnHandModelForm
from cash.models import CashOnHand

logger = logging.getLogger(__name__)


class IndexView(generic.ListView):
    template_name = 'cash/cashindex.html'
    context_object_name = 'cash_list'

    def get_queryset(self):
        return CashOnHand.objects.all()


class DetailView(generic.DetailView):
    model = CashOnHand
    context_object_name = 'cash_on_hand'
    template_name = 'cash/detail.html'


class CreateView(generic.edit.CreateView):
    # model = CashOnHand
    # fields = ['operation_date', 'serial_number', 'opposite_account', 'summary', 'lucre', 'remark']
    template_name = 'cash/add.html'
    form_class = CashOnHandModelForm
    model = CashOnHand
    success_url = reverse_lazy('cash:index')


class UpdateView(generic.edit.UpdateView):
    model = CashOnHand
    fields = ['operation_date', 'serial_number', 'opposite_account', 'summary', 'lucre', 'remark']
    template_name_suffix = '_update_form'
    # template_name = 'cash/edit.html'
    success_url = reverse_lazy('cash:index')


class DeleteView(generic.edit.DeleteView):
    model = CashOnHand
    success_url = reverse_lazy('cash:index')


@login_required
def login_view(request):
    return render(request, 'cash/child1.html')


def logout_view(request):
    logout(request)
    # Redirect to a success page.
