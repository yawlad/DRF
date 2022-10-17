from dataclasses import fields
from pyexpat import model
from django_filters import rest_framework as filters
from .models import User

class UserFilter(filters.FilterSet):
    
    username = filters.CharFilter(lookup_expr="contains")
    first_name = filters.CharFilter(lookup_expr="contains")
    last_name = filters.CharFilter(lookup_expr="contains")
    email = filters.CharFilter(lookup_expr="contains")
    age = filters.Filter()
    
        