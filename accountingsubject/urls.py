from django.urls import path
from . import views

app_name = 'subject'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:accounting_subject_id>/edit/', views.accounting_subject_edit, name='edit'),
]
