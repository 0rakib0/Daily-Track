from django.urls import path
from . import views

app_name='utils'

urlpatterns = [
    path('add-budget-category/', views.add_budget_cat, name='add_budget_cat'),
    path('budget-category-list/', views.view_budget_category, name='category_list'),
    path('add-budget/', views.add_badget, name='add_budget'),
    path('view-budget-list/', views.view_budget, name='view_budget'),
    path('delete-budget-category/<id>/', views.delete_budget_cat, name='delete_category'),
    path('update-to-complate/<id>/', views.update_to_complate, name='update_to_complate'),
    path('delete-budget/<id>/', views.delete_budget, name='delete_budget'),
    path('shedule-mail/', views.SendMail, name='send_mail'),
    path('sent-mail-list/', views.SentMail, name='sent_mail'),
    path('delete-mail/<id>/', views.DeleteMail, name='delete_mail'),
]