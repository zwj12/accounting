import logging
import json
from datetime import date

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from cash.forms import CashOnHandForm, CashOnHandModelForm
from cash.models import CashOnHand

logger = logging.getLogger(__name__)


class IndexView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'cash.view_cashonhand'
    raise_exception = False
    permission_denied_message = "You are not allowed"
    # permission_required = ''
    template_name = 'cash/index.html'
    context_object_name = 'cash_list'
    paginate_by = 10

    def get_queryset(self):
        return CashOnHand.objects.all()


class DetailView(LoginRequiredMixin, generic.DetailView):
    permission_required = 'cash.view_cashonhand'
    model = CashOnHand
    context_object_name = 'cash_on_hand'
    template_name = 'cash/detail.html'


class CreateView(PermissionRequiredMixin, generic.edit.CreateView):
    permission_required = 'cash.add_cashonhand'
    # model = CashOnHand
    # fields = ['operation_date', 'serial_number', 'opposite_account', 'summary', 'lucre', 'remark']
    template_name = 'cash/add.html'
    form_class = CashOnHandModelForm
    model = CashOnHand
    success_url = reverse_lazy('cash:index')

    def get_initial(self):
        self.initial = {}
        if 'operation_date' in self.request.session:
            self.initial['operation_date'] = date.fromisoformat(self.request.session['operation_date'])
        if 'opposite_account' in self.request.session:
            self.initial['opposite_account'] = self.request.session['opposite_account']
        return self.initial

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.request.session['operation_date'] = form.instance.operation_date.isoformat()
        self.request.session['opposite_account'] = form.instance.opposite_account.id
        return super().form_valid(form)


class UpdateView(generic.edit.UpdateView):
    permission_required = 'cash.change_cashonhand'
    model = CashOnHand
    fields = ['operation_date', 'serial_number', 'opposite_account', 'summary', 'lucre', 'remark']
    template_name_suffix = '_update_form'
    # template_name = 'cash/edit.html'
    success_url = reverse_lazy('cash:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.request.session['operation_date'] = form.instance.operation_date.isoformat()
        self.request.session['opposite_account'] = form.instance.opposite_account.id
        return super().form_valid(form)


class DeleteView(generic.edit.DeleteView):
    permission_required = 'cash.delete_cashonhand'
    model = CashOnHand
    success_url = reverse_lazy('cash:index')


@login_required
@permission_required('cash.add_cashonhand', raise_exception=True)
def login_view(request):
    return render(request, 'cash/child1.html')


def logout_view(request):
    logout(request)
    # Redirect to a success page.
