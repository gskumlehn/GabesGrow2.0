from django.urls import path
from apps.config.views import index

urlpatterns = [
    path('', index, name='config'),
]
