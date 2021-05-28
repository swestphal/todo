from django.shortcuts import render

from .models import Task
from .serializers import TaskSerializer

from rest_framework import viewsets
from rest_framework.authentication import  BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer