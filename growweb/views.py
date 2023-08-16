from django.shortcuts import render

def index(request):
    return render(request, 'growweb/index.html')
def data(request):
    return render(request, 'growweb/data.html')
