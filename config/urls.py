from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authapp.views import UserModelViewSet
from todoapp.views import ToDoModelViewSet, ProjectModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('todos', ToDoModelViewSet)
router.register('projects', ProjectModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    
]
