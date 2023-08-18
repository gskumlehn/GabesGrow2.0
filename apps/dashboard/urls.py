from django.urls import path
from apps.dashboard.views import data, index

urlpatterns = [
    path('', index, name='index'),
    path('data', data, name='data'),
]
