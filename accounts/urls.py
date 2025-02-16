from django.urls import path
from . import views

urlpatterns = [
    path('login-page/', views.Login_page, name='login_page'),
    path('register-user/', views.register_user, name='register_user'),
    path('logout-user/', views.user_logout, name='logout'),
    path('update-profile/', views.update_profile, name='update_profile')
]
