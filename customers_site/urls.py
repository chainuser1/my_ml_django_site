_author__ = 'Lotus Corporation'

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name="customers"

urlpatterns = [
    path('home/', views.index, name="home"),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('view_cart_item_list', views.view_cart_item_list, name="view_cart_item_list")
]
