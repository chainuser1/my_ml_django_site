from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=17,required=True ,widget=forms.TextInput(attrs={'class':'form-control fadeIn second','placeholder':'Username'}))
    first_name = forms.CharField(max_length=50, required=True,widget=forms.TextInput(attrs={'class':'form-control fadeIn third','placeholder':'First Name'}))
    last_name = forms.CharField(max_length=50, required=True,widget=forms.TextInput(attrs={'class':'form-control fadeIn second', 'placeholder':'Last Name'}))
    password1 = forms.CharField(max_length=25, required=True,min_length=10 ,widget=forms.PasswordInput(attrs={'class':'form-control fadeIn second','placeholder':'Password'}))
    email = forms.EmailField(max_length=35, required=True,widget=forms.EmailInput(attrs={'class':'form-control fadeIn second', 'placeholder':'Email'}))
    password2 = forms.CharField(max_length=25, required=True,min_length=10 ,widget=forms.PasswordInput(attrs={'class':'form-control fadeIn third','placeholder':'Confirm Password'}))
    
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email','password1', 'password2']