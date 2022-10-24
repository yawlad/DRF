from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from authapp.views import UserModelViewSet  #CustomPermissionUserModelViewSet
from todoapp.views import ToDoModelViewSet, ProjectModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('todos', ToDoModelViewSet)
router.register('projects', ProjectModelViewSet)
# router.register('admin-users', CustomPermissionUserModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth_token/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls')),
    
]
