__author__ = 'Lotus Corporation'

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name="login"

urlpatterns = [
    path('do/', views.login_do, name="login_do"),
    path('lico-auth/',views.auth, name='lico_auth'),
    path('lico-logout/', views.sign_out, name='lico_logout'),
    path('auth-register/', views.register, name='lico_register'),
    # path('accounts/login', auth_views.LoginView.as_view(), name='login'),
    # path('auth-create-lico', views.store, name='lico_store'),
]
