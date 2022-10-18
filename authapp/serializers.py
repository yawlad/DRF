from dataclasses import fields
from rest_framework.serializers import ModelSerializer, RelatedField
from .models import User

class UserModelSerializer(ModelSerializer):

    class Meta: 
        model = User
        fields = ['username']
        fields = ['id', 'username', 'first_name', 'last_name', 'age', 'email']
    
class UserModelListingField(RelatedField):

    def to_representation(self, value):
        return value.username

