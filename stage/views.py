from django.shortcuts import render
from stage.models import Stage

def show(request):
    return render(request, 'stage/show.html')

def list(request):
    stages = Stage.objects.all()
    return render(request, 'stage/list.html', {"stages": stages})
