import logging

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import generic

from cash.models import CashOnHand

logger = logging.getLogger(__name__)


def results(request, accounting_subject_id):
    return HttpResponse("You're looking at the results of accounting subject %s." % accounting_subject_id)

