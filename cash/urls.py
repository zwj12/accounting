from django.urls import path

from . import views

app_name = 'cash'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('accountingsubject/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('accountingsubject/<int:accounting_subject_id>/edit/', views.accounting_subject_edit, name='accountingsubjectedit')
]
