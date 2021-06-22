
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import  never_cache
from django.shortcuts import render #get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Product, Category, Log
from django.contrib.auth.models import User
from datetime import datetime
# Create your views here.


@login_required(redirect_field_name='next', login_url = 'login:login_do')
@never_cache
def home(request):
    return render(request, 'index.html')

# query products and send as json

def products(request):
    return JsonResponse({'products':list(Product.objects.all().values())},safe=False)
# query categories and send as json
def categories(request):
    return JsonResponse({'categories':list(Category.objects.all().values())},safe=False)


# create product according to existing
@login_required(redirect_field_name='next', login_url = 'login:login_do')
def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        category_id = request.POST['category']
        stock = request.POST['stock']
       
        try:
            category = Category.objects.get(pk=category_id)
            new_product = category.product_set.create(name=name,price=price,stock=stock)
            return JsonResponse({'message':new_product.name + ' has been created.'})
        except Category.DoesNotExist:
            return JsonResponse({'message':'An error occurred.'})
    else:
        return JsonResponse({'message':'An error occurred'})

# Update Product 
@login_required(redirect_field_name='next', login_url = 'login:login_do')
def update(request,id):
    if request.method == 'POST':
        try:
            Product.objects.filter(pk=id).update(name = request.POST["name"],
            price = request.POST["price"],
            category= request.POST["category"],
            stock = request.POST["stock"],
            updated_at = datetime.now())
            pro_obj = Product.objects.filter(pk=id).get()
            Log.objects.create(transaction_name="Product Update",
                       transaction_details=pro_obj.name + ' has been updated.',
                       user=request.user)
            
            return JsonResponse({'message': pro_obj.name + ' has been updated.'})
        except Product.DoesNotExist:
            return JsonResponse({'message':'An error occurred while updating product. The product does not exist'})

#delete products
@login_required(redirect_field_name='next', login_url = 'login:login_do')
def delete(request, id):
    if request.method == 'POST':
        try:
            obj_deleted = Product.objects.filter(pk=id).get()
            Product.objects.filter(pk=id).delete()
            return JsonResponse({'message': obj_deleted.name + ' was successfully deleted.'})
        except Product.DoesNotExist:
            return JsonResponse({'message': 'An error occurred while deleting product. This product is not found'})


@login_required(redirect_field_name='next', login_url = 'login:login_do')
def show_logs(request):
    logs = Log.objects.all().order_by("-created_at").values()
    logs=list(logs)
    return JsonResponse({'logs':logs}, safe=False)

