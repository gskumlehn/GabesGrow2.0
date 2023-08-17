from django.shortcuts import render
from user.forms import LoginForm
def login(request):
    form = LoginForm()
    return render(request, 'user/login.html', {"form": form})