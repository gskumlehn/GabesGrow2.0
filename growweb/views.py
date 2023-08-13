from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Gabe`s Grow 2.0</h1>')
