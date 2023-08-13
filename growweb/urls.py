from django.urls import path
from growweb.views import index

urlpatterns = [
    path('', index),
]
