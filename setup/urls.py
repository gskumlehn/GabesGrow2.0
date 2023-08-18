"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('config/', include('apps.config.urls')),
    path('', include('apps.dashboard.urls')),
    path('stage/', include('apps.stage.urls')),
    path('', include('apps.user.urls')),
]
