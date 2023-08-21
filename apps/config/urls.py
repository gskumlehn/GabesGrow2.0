from django.urls import path
from apps.config.views import index

urlpatterns = [
    path('<int: config_id>', index, name='config'),
]
