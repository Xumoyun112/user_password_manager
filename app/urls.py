from django.urls import path, include
from .views import UserPasswordManagerModelViewSet
from rest_framework.routers import DefaultRouter

r = DefaultRouter()

r.register(r'app', UserPasswordManagerModelViewSet, basename='userpass')
urlpatterns = [
    path('', include(r.urls))
]
