from django.contrib.auth.decorators import login_required
from django.shortcuts import render ,get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from verify_email.email_handler import send_verification_email #install https://pypi.org/project/Django-Verify-Email/
from .forms import RegisterForm
# Create your views here.

@login_required(redirect_field_name='next', login_url = 'login:login_do')
def sign_out(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@never_cache
def login_do(request):
    response = redirect('survey_app:home')
    if request.user.is_authenticated:
        try:
            if("next" in request.session):
                response =  redirect(request.session["next"])
        except KeyError:
            response = response
    else:
        response = render(request,'login/login.html')
    return response


@never_cache
def auth(request):
    response = redirect('survey_app:home')
   
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if(user is not None):
            login(request, user)
            try:
                if("next" in request.session):
                    response =  redirect(request.session["next"])
            except KeyError:
                response = HttpResponse('I don\'t know where to go')
        return response
    else:
        response = HttpResponse('Invalid request')
    return response


@never_cache
def register(request):
    if request.user.is_authenticated:
        return redirect(reverse("survey_app:home"))
    form = RegisterForm(request.POST or None)
    response =  None
    if(request.POST and form.is_valid()):
        try:
            inactive_user = send_verification_email(request, form)
            if("next" in request.session):
                response=redirect(request.session["next"])
            else:
                response=redirect('survey_app:home')
        except Exception:
            response = HttpResponse("Error occurred when verifying your email address.")
    else: 
        response = render(request, 'login/register.html', {'form':form})
    return response
    