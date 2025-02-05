from django.urls import path
from . import views

app_name='utils'

urlpatterns = [
    path('add-budget-category/', views.add_budget_cat, name='add_budget_cat')
]