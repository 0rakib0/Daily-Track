from django.urls import path
from . import views

app_name='transaction'

urlpatterns = [
    path('add-bank/', views.AddBank, name='add_bank'),
    path('view-bank-accounts/', views.View_Banks, name='view_bank')
]