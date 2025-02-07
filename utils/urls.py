from django.urls import path
from . import views

app_name='utils'

urlpatterns = [
    path('add-budget-category/', views.add_budget_cat, name='add_budget_cat'),
    path('budget-category-list/', views.view_budget_category, name='category_list'),
    path('add-budget/', views.add_badget, name='add_budget'),
    path('view-budget-list/', views.view_budget, name='view_budget'),
]