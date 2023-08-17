from django.urls import path
from dashboard.views import index

urlpatterns = [
    path('config', config, name='config'),
]
