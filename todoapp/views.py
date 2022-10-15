from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# Create your views here.


from .serializers import ProjectModelSerializer, ToDoModelSerializer
from .models import Project, ToDo

class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer

class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer