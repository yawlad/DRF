from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import UpdateModelMixin, ListModelMixin
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .filters import UserFilter


from .serializers import UserModelSerializer
from .models import User

class UserModelViewSet(ListModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    filterset_class = UserFilter
    
    