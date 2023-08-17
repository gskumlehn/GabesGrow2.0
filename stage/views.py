from django.shortcuts import render

def show(request):
    return render(request, 'stage/show.html')

def list(request):
    return render(request, 'stage/list.html')
