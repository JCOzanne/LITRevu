from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect, render

from . import forms

def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Identifiants invalides.'
    return render(request, 'authentication/login.html', context={'form': form, 'message': message})


def logout_user(request):
    logout(request)
    return redirect ('login')

def signup_page(request):
    form = forms.SignUpForm()
    if request.method =='POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect (settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})

