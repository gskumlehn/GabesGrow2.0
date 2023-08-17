from django.urls import path
from config.views import index

urlpatterns = [
    path('config', index, name='config'),
]
