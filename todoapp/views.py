from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticatedOrReadOnly 


from .serializers import ProjectModelSerializer, ToDoModelSerializer
from .models import Project, ToDo
from .paginators import ProjectLimitOffsetPagination, ToDoLimitOffsetPagination

class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    pagination_class = ProjectLimitOffsetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    pagination_class = ToDoLimitOffsetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        to_do = self.get_object()
        to_do.deleted = True
        to_do.save()
        return Response(status=status.HTTP_200_OK)


