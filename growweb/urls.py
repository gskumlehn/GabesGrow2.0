from django.urls import path
from growweb.views import index, data

urlpatterns = [
    path('', index, name='index'),
    path('data/', data, name='data'),
]
