# tasks/urls.py

from django.urls import path
from .views import (
    register_view,
    login_view,
    account_details,
    logout_view,
    home_view,
    change_password_view,
    delete_account_view
)

app_name = 'tasks'  # Define el namespace correctamente

urlpatterns = [
    path('', home_view, name='index'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('account/', account_details, name='account_details'),
    path('logout/', logout_view, name='logout'),
    path('change-password/', change_password_view, name='change_password'),
    path('delete/', delete_account_view, name='delete_account'),
]
