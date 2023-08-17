from django.urls import path
from dashboard.views import data, index

urlpatterns = [
    path('', index, name='index'),
    path('', data, name='data'),
]
