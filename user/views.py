from dashboard.views import index
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from user.forms import LoginForm
import logging

def login(request):
    form = LoginForm()
    logger = logging.getLogger("mylogger")
    logger.info('ooooooooooooooooooi')
    if request.method == 'POST':
        if form.is_valid():

            username = form.username.value()
            password = form.password.value()

            user = auth.authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect(index)
            else:
                return redirect(login)

    return render(request, 'user/login.html', {"form": form})