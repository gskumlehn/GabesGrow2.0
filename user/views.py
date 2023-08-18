from dashboard.views import index
from django.contrib.auth.models import auth
from django.shortcuts import render, redirect
from user.forms import LoginForm

def login(request):
    form = LoginForm()

    if request.method == 'POST':
        if form.is_valid():

            username = form['username'].value()
            password = form['password'].value()

            user = auth.authenticate(request, username=username, password=password)

            if user:
                auth.login(request, user)
                return redirect(index)
            else:
                return redirect(login, {"user": user is not None})

    return render(request, 'user/login.html', {"form": form})