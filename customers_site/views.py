from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import  never_cache
from django.shortcuts import render ,get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from survey_app.models import Product, Category, Log
from django.contrib.auth.models import User
from datetime import datetime
from django.core.serializers import serialize
import json, time, numpy as np
from django.core.exceptions import ObjectDoesNotExist
from .models import Cart, Item, Preference
# Create your views here.

@login_required(login_url='login:login_do',   redirect_field_name='next')
def index(request):
    """ 
        Index page
    """
    return render(request, 'customers_site/home.html')

def add_to_cart(request):
    """
       Add cart item to the cart
    """
    cart = None
    try:
        cart = Cart.objects.get(user_id=request.user.id)
    except ObjectDoesNotExist:
        cart = Cart(user=request.user)
        cart.save()
    new_item = cart.item_set.create(product = get_object_or_404(Product,name=request.POST['product']), quantity=request.POST['quantity'], price_ht=request.POST['price'])
    return JsonResponse({'message': new_item.product.name + ' added to cart'})
    
def view_cart_item_list(request):
    cart = Cart.objects.get(user_id=request.user.id)
    items = cart.item_set.all()
    items = serialize('json',items, use_natural_foreign_keys=True)
    return JsonResponse({'items':json.loads(items)}, safe=False)