from django.urls import path
from . import views

urlpatterns = [
    path('login-page/', views.Login_page, name='login_page')
]
