from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages #display message after logging in/out


def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')

def UserSignUp(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form= SignUpForm()
    return render(request, 'core/signup.html',{
         'form': form
    })

def PLogIn(request):
    return render(request, 'core/elogin.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You are now logged out")
    return redirect('/')




