from django.urls import path
from . import views

app_name='transaction'

urlpatterns = [
    path('add-bank/', views.AddBank, name='add_bank')
]