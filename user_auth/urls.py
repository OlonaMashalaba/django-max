from django.urls import path
from . import views

app_name = 'user_auth'

urlpatterns = [
    path('', views.user_login, name='login'),
    path('register/', views.register_user, name='register_user'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
]