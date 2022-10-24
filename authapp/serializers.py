from dataclasses import fields
from rest_framework.serializers import ModelSerializer, RelatedField
from .models import User

class UserModelSerializer(ModelSerializer):

    class Meta: 
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'age', 'email']
    
class UserModelListingField(RelatedField):

    def to_representation(self, value):
        return value.username

# class CustomPermissionUserModelSerializer(ModelSerializer):

#     class Meta: 
#         model = User
#         fields = '__all__'