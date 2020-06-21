from django.views import generic

from cash.models import CashOnHand


class IndexView(generic.ListView):
    template_name = 'cash/cashindex.html'
    context_object_name = 'cash_list'

    def get_queryset(self):
        return CashOnHand.objects.all()