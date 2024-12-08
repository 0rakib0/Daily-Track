from django.urls import path
from . import views

app_name='transaction'

urlpatterns = [
    path('add-bank/', views.AddBank, name='add_bank'),
    path('view-bank-accounts/', views.View_Banks, name='view_bank'),
    path("update/<int:id>/", views.UpdateBank, name="update_bank"),
    path('delete-bank/<int:id>/', views.DeleteBank, name='delete_bank'),
    path('deposit-blance/', views.deposit_blance, name='deposit_blance'),
    path('transection-amount/', views.transection_blance, name='transection_blance'),
    path('add-income/', views.Add_Income, name='add_income'),
    path('add-express/', views.Add_Express, name='add_express'),
    path('view-income/', views.View_Income, name='view_income'),
    path('update-income-data/<int:id>/', views.UpdateIncome, name='update_incom'),
    path('delete-income/<int:id>/', views.DeleteIncome, name='delete_income'),
    path('view-express/', views.View_Express, name='view_express'),
    path('update-express-data/<int:id>/', views.UpdateExpress, name='update_express'),
    path('delete-expess/<int:id>/', views.DeleteExpress, name='delete_express'),
]