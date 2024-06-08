from django.shortcuts import render,redirect

from .forms import RegistationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def home(request):
    return render(request,'./home.html')
def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
          form = RegistationForm(request.POST)
          if form.is_valid():
            messages.success(request,'account created succesfully')
            form.save()
            print(form.cleaned_data)
        else:
            form = RegistationForm()
        return render(request,'account/signup.html',{'form':form})
    else:
        return redirect('recommend_universities')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username=name,password=userpass)
                if user is not None:
                    login(request,user)
                    return redirect('recommend_universities')
        else:
            form = AuthenticationForm()
        return render(request,'account/login.html',{'form':form})
    else:
        return redirect('profilepage')

def user_profile(request):
    return render(request,'account/profile.html')
    
def user_logout(request):
    logout(request)
    return redirect('loginpage')


    
