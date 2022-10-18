from dataclasses import fields
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Project, ToDo
from authapp.serializers import UserModelListingField

class ProjectModelSerializer(ModelSerializer):
    users = UserModelListingField(many=True, read_only=True)
    class Meta: 
        model = Project
        fields = '__all__'

class ToDoModelSerializer(ModelSerializer):

    class Meta: 
        model = ToDo
        fields = '__all__'