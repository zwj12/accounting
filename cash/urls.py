from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'cash'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('accountingsubject/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('accountingsubject/<int:accounting_subject_id>/edit/', views.accounting_subject_edit, name='accountingsubjectedit'),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
]
