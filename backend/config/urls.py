from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.permissions import IsAuthenticated

from todoapp.views import ToDoModelViewSet, ProjectModelViewSet
from authapp.views import UserModelViewSet  #CustomPermissionUserModelViewSet

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from todoapp.views import ToDoModelViewSet, ProjectModelViewSet


from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from graphene_django.views import GraphQLView

schema_view = get_schema_view(
    openapi.Info(
        title='ToDoApp',
        default_version='v1',
        description='Application to make todos',
        license=openapi.License(name='MIT LICENSE'),
        contact=openapi.Contact(name='Vlad', email='y.yawlad@gmail.com')
    ),
    public=True,
    permission_classes=(IsAuthenticated,),
)

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('todos', ToDoModelViewSet)
router.register('projects', ProjectModelViewSet)

# router.register('admin-users', CustomPermissionUserModelViewSet)

# router.register()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    
    path('api/auth_token/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls')),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('swagger/', schema_view.with_ui('swagger')),
    path('redoc/', schema_view.with_ui('redoc')),

    path('graphql/', GraphQLView.as_view(graphiql=True)),
    
    path("", TemplateView.as_view(template_name="index.html"))
]
