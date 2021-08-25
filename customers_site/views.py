from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import  never_cache
from django.shortcuts import render #get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from survey_app.models import Product, Category, Log
from django.contrib.auth.models import User
from datetime import datetime
from django.core.serializers import serialize
import json, time, numpy as np


@login_required(login_url='login:login_do',   redirect_field_name='next')
def index(request):
    return render(request, 'customers_site/home.html')

def add_to_cart(request):
    pass