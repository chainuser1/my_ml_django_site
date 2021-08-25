_author__ = 'Lotus Corporation'

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name="customers"

urlpatterns = [
    path('home/', views.index, name="home"),
    # path('accounts/login', auth_views.LoginView.as_view(), name='login'),
    # path('auth-create-lico', views.store, name='lico_store'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
]
