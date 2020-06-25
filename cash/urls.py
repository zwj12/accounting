from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import UpdateView, DeleteView, DetailView, CreateView

app_name = 'cash'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('accountingsubject/<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('accountingsubject/<int:accounting_subject_id>/edit/', views.accounting_subject_edit, name='accountingsubjectedit'),
    # path('accounts/login/', auth_views.LoginView.as_view()),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('cash/child', views.child, name='childx'),
    path('cash/<int:pk>/', DetailView.as_view(), name='detail'),
    path('cash/add/', CreateView.as_view(), name='add'),
    path('cash/<int:pk>/edit/', UpdateView.as_view(), name='edit'),
    path('cash/<int:pk>/delete/', DeleteView.as_view(), name='delete'),
]
