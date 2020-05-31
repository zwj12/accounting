from django.urls import path

from . import views

app_name = 'cash'
urlpatterns = [
    path('', views.index, name='index'),
    path('accountingsubject/<int:accounting_subject_id>/', views.detail, name='detail'),
    path('accountingsubject/<int:accounting_subject_id>/edit', views.accounting_subject_edit, name='accountingsubjectedit')
]
