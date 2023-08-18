from django.contrib.auth.models import auth
from django.contrib import messages
from django.shortcuts import render, redirect
from user.forms import LoginForm

def login(request):
    form = LoginForm()

    if request.user:
        return redirect('index')

    if request.method == 'POST':
        if form.is_valid():

            user = auth.authenticate(request, username=form.username, password=form.password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, "login successful")
                return redirect('index')
            else:
                messages.error(request, "login failed")
                return redirect('login')

    return render(request, 'user/login.html', {"form": form})

def logout(request):
    auth.logout(request)
    return redirect('index')