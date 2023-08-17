from django.shortcuts import render

def index(request):
    temperature = 22.00
    return render(request, 'growweb/index.html', {"temperature": temperature})
def data(request):
    return render(request, 'growweb/data.html')
