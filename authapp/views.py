from pyexpat import model
from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import UpdateModelMixin, ListModelMixin
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.permissions import IsAdminUser

from django.views import View

from .filters import UserFilter
from .permissions import IsAdmin ###-CUSTOM_PERMISSIONS-###

from .serializers import UserModelSerializer, UserModelSerializerVersion1 #CustomPermissionUserModelSerializer
from .models import User


class UserModelViewSet(ListModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    filterset_class = UserFilter
    
    def get_serializer_class(self):
        if self.request.version == 'v1':
            return UserModelSerializerVersion1
        return UserModelSerializer

# class CustomPermissionUserModelViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = CustomPermissionUserModelSerializer
#     filterset_class = UserFilter
#     permission_classes = [IsAdmin, IsAdminUser]

    