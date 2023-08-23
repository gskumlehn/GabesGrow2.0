from django.urls import path
from apps.config.views import index, edit

urlpatterns = [
    path('<int:config_id>', index, name='config'),
    path('edit/<int:config_id>', edit, name='editConfig'),
]
