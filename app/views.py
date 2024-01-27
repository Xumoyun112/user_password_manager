from django.shortcuts import render
from .serializers import UserPasswordManagerSerializer
from .models import UserPasswordManager
from rest_framework import viewsets

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class UserPasswordManagerModelViewSet(viewsets.ModelViewSet):
    queryset = UserPasswordManager.objects.all()
    serializer_class = UserPasswordManagerSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields =['name']
    filterset_fields = ['application_type']

