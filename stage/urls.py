from django.urls import path
from stage.views import show

urlpatterns = [
    path('stage', show, name='show'),
]
