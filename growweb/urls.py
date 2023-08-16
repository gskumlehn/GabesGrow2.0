from django.urls import path
from growweb.views import index, data

urlpatterns = [
    path('', index),
    path('data/', data),
]
